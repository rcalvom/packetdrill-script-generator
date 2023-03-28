""" Execute Tests"""

# System
import configuration
import subprocess
import threading
import traceback
import logging
import shutil
import signal
import time
import os

# Script generator
import configuration

# Variables
execution_cancelled = False


def execute_test(folder, packetdrill_command, target):
    """
    Execute all test of generated scripts
    """
    threads = []
    for i in range(configuration.number_runners):
        directory_path = create_directory(folder, "consumer{:02d}".format(i))
        thread = threading.Thread(target=execute_script, args=(directory_path, packetdrill_command, target, i), daemon=True)
        thread.start()
        threads.append(thread)
    signal.signal(signal.SIGINT, sigint_handler)
    for thread in threads:
        thread.join()


def execute_script(directory_path, packetdrill_command, target, id):
    """
    Consumer Thread. Execute a set of scripts
    """
    target_process = None
    # try:
    interface_name = "tap{0}".format(id) #TODO: https://pypi.org/project/python-pytuntap/
    if not os.path.exists("/sys/class/net/{0}".format(interface_name)):
        logging.error("Virtual TAP interface '{0}' not found.".format(interface_name))
        return
    logging.debug("Starting on virtual interface {0}.".format(interface_name))
    env_variables = {
        'TAP_INTERFACE_NAME': interface_name
    }
    index_file_name = os.path.abspath(os.path.join(directory_path, "index.txt"))
    while not execution_cancelled:
        with open(index_file_name, 'w') as index_file:
            index_file.write('')
        while True:
            with open(index_file_name, 'r') as index_file: #TODO: File reading is slow, memory?
                index_file_content = index_file.read()
                if "Completed" in index_file_content:
                    logging.debug("Completed found.")
                    break
                elif "Finished" in index_file_content:
                    finish_execution(target_process)
        scripts = [os.path.abspath(os.path.join(directory_path, f)) for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f)) and not f.endswith("index.txt")]
        for script in scripts:
            logging.debug("Running script {0}".format(script))

            hang = False

            # Start project A if it's not already running
            if target_process is None or target_process.poll() is not None:
                target_process = subprocess.Popen(target, env=env_variables)
                logging.debug("Target started")

            try:
                pd_command_copy = packetdrill_command[:]
                pd_command_copy.append(script)
                logging.debug(pd_command_copy)
                subprocess.run(pd_command_copy, env=env_variables, timeout=2)
                logging.debug("Packetdrill command completed")
            except subprocess.TimeoutExpired:
                # If process B times out, kill both processes and write the command to "hang.txt"
                logging.debug("PD command timed out... Killing processes")
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
                logging.debug("Target process stopped. Writing input")
                shutil.copy2(script, configuration.crash_dir)

            # If target is not running, wait for 2 seconds before restarting
            if target_process.poll() is not None:
                time.sleep(2)

        recreate_folder(directory_path)

    logging.debug("Terminating thread")
    finish_execution(target_process)
    # except threading.ThreadError:
    #     finish_execution(target_process)



def create_directory(path, name):
    """
    Create directory
    """
    dir_path = os.path.join(path, name)
    if (not os.path.exists(dir_path)):
        os.makedirs(dir_path)
    else:
        index_file_path = os.path.join(dir_path, 'index.txt')
        if os.path.exists(index_file_path):
            os.remove(index_file_path)
    return dir_path

def recreate_folder(folder):
    """
    Recreate folder
    """
    shutil.rmtree(folder)
    os.mkdir(folder)


def sigint_handler(sig, frame):
    """
    Function to handle exit command.
    """
    global execution_cancelled
    logging.debug("Interrupting Execution.")
    print("Ctrl + C pressed. Signalling all threads to stop.")
    execution_cancelled == True
    exit()
    # for thread in threading.enumerate():
    #     if thread != threading.current_thread():
    #         thread.stop()


def finish_execution(target):
    """
    Stop a given target
    """
    logging.debug("Finishing Execution")
    if target is not None and target.poll() is None:
        target.kill()
    exit()


def finish_execution(target):
    """
    Stop a given target
    """
    logging.debug("Finishing Execution")
    if target is not None and target.poll() is None:
        target.kill()
    exit()