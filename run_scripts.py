import configuration
import os
import shutil
import signal
import subprocess
import threading
import time
import traceback

from utils import debug_print

execution_cancelled = False

def sigint_handler(sig, frame):
    global execution_cancelled
    debug_print("Interrupting Execution...")
    print("Ctrl+C pressed. Signalling all threads to stop...")
    # for thread in threading.enumerate():
    #     if thread != threading.current_thread():
    #         thread.stop()
    execution_cancelled == True
    exit()

def delete_all_files(folder):
    scripts = [os.path.abspath(os.path.join(folder, f)) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

    for script in scripts:
        try:
            os.remove(script)
            print("Deleted file: %s" % script)
        except OSError as e:
            print("Error deleting file: %s - %s." % (script, e.strerror))

def finish_execution(target):
    debug_print("Finishing Execution")
    # Stop any running target instance
    if target is not None and target.poll() is None:
        target.kill()
    exit()
   

def execute_script(folder, pd_command: list, target, id):

    target_process = None

    # try:

    interface_name = f"tap{id}"
    if not os.path.exists(f"/sys/class/net/{interface_name}"):
        debug_print(f"Error: virtual TAP interface '{interface_name}' not found.")
        return

    debug_print(f"Starting test execution {id} on virtual interface {interface_name}")

    env_variables = {'TAP_INTERFACE_NAME': interface_name}

    index_file_name = os.path.abspath(os.path.join(folder, "index.txt"))

    while not execution_cancelled:

        # Create index.txt
        with open(index_file_name, 'w') as index_file:
            index_file.write('')

        # Wait on index.txt till completed is written on it
        while True:
            with open(index_file_name, 'r') as index_file:
                index_file_content = index_file.read()

                if "Completed" in index_file_content:
                    debug_print("Completed found")
                    break
                elif "Finished" in index_file_content:
                    finish_execution(target_process)

        # Retrieve scripts and run tests

        scripts = [os.path.abspath(os.path.join(folder, f)) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)) and not f.endswith("index.txt")]
        
        for script in scripts:

            debug_print(f"Running script {script}")

            hang = False

            # Start project A if it's not already running
            if target_process is None or target_process.poll() is not None:
                target_process = subprocess.Popen(target, env=env_variables)
                debug_print("Target started")

            try:
                pd_command_copy = pd_command[:]
                pd_command_copy.append(script)
                debug_print(pd_command_copy)
                subprocess.run(pd_command_copy, env=env_variables, timeout=2)
                debug_print("Packetdrill command completed")
            except subprocess.TimeoutExpired:
                # If process B times out, kill both processes and write the command to "hang.txt"
                debug_print("PD command timed out... Killing processes")
                hang = True
                if target_process.poll() is not None:
                    # There was a crash that caused this hangout
                    shutil.copy2(script, configuration.crash_dir)
                else:
                    # This was just a weird hang but the target is still running so we kill it
                    target_process.kill()
                    shutil.copy2(script, configuration.hang_dir)
                
            except Exception as ex:
                # Catch other exeptions and kill running process
                traceback.print_exc()
                finish_execution(target_process)

            # The target crashed but for some reason, it didn't cause a timeout
            if target_process.poll() is not None and hang is False:
                debug_print("Target process stopped. Writing input")
                shutil.copy2(script, configuration.crash_dir)

            # If target is not running, wait for 2 seconds before restarting
            if target_process.poll() is not None:
                time.sleep(2)

        # Delete all files in directory
        delete_all_files(folder)

    debug_print("Terminating thread")
    finish_execution(target_process)
    # except threading.ThreadError:
    #     finish_execution(target_process)



def create_directory(path, name):
    dir_path = os.path.join(path, name)
    if (not os.path.exists(dir_path)):
        os.makedirs(dir_path)
    else:
        index_file_path = os.path.join(dir_path, 'index.txt')
        if os.path.exists(index_file_path):
            os.remove(index_file_path)
    return dir_path


def execute_test(folder, pd_command: list, target):
    n = 3
    threads = []

    # For each consumer, we create a directory and start a new thread to run the script
    for i in range(n):

        dir_path = create_directory(folder, f"consumer{i:02d}")
        thread = threading.Thread(target=execute_script, args=(dir_path, pd_command, target, i))
        threads.append(thread)
        thread.daemon = True
        thread.start()

    signal.signal(signal.SIGINT, sigint_handler)
    for thread in threads:
        thread.join()