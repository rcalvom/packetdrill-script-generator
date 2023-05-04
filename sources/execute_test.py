""" Functions to execute Packetdrill """

# System
import threading
import subprocess
import datetime
import logging
import shutil
import copy
import time
import os

# Script generator
import sources.generate_scripts
import configuration
import test_cases as tests

# Constants
interface_name_env = 'TAP_INTERFACE_NAME'
packetdrill_trace_suffix = '.packetdrill.log'
target_trace_suffix = '.target.log'
target_timeout = 2.0


# Variables
semaphore = threading.Semaphore(configuration.number_runners)
templates = sources.generate_scripts.preload_templates(configuration.templates_filenames)
test_cases = tests.test_cases
count = 0
current_count = 0
total_count = 0
initial_timestamp = None
current_timestamp = None
slots = {}


def execute_list_scripts(folder):
    global count, total_count, current_count, templates, semaphore
    scripts = os.listdir(folder)
    for script in scripts:
        count += 1
        if count < configuration.start_test_count:
            continue
        if count >= configuration.end_test_count:
            continue
        current_count += 1
        if current_count % 100 == 0:
            with open(os.path.join(configuration.output_directory, "stats.log"), "w+") as f:
                current_timestamp = datetime.datetime.fromtimestamp(time.time())
                time_difference = current_timestamp - initial_timestamp
                f.write("*Execution in progress*\n")
                f.write("Total count: {0}\n".format(total_count))
                f.write("Current count: {0}\n".format(current_count))
                f.write("Progress: {0:.2f}% ({1} / {2})\n".format(current_count / total_count * 100, current_count, total_count))
                f.write("Initial timestamp: {0}\n".format(initial_timestamp))
                f.write("Current timestamp: {0}\n".format(current_timestamp))
                f.write("Executing time: {0} hours, {1} minutes, {2} seconds. \n".format(time_difference.seconds // 3600, (time_difference.seconds % 3600) // 60, time_difference.seconds % 60))
        script_path = os.path.join(configuration.generated_folder, script)
        semaphore.acquire() 
        assign_to_thread(script_path)


def execute_and_generate_test():
    """
    Generate and execute at same time the tests
    """
    global count, total_count, slots, initial_timestamp
    initial_timestamp = datetime.datetime.fromtimestamp(time.time())
    slots = init_slots()
    count_cases(configuration.generated_folder)
    execute_list_scripts(configuration.generated_folder) 
    with open(os.path.join(configuration.output_directory, "stats.log"), "w+") as f:
        current_timestamp = datetime.datetime.fromtimestamp(time.time())
        time_difference = current_timestamp - initial_timestamp
        f.write("*Execution Finished*\n")
        f.write("Total count: {0}\n".format(total_count))
        f.write("Final count: {0}\n".format(current_count))
        f.write("Progress: {0:.2f}% ({1} / {2})\n".format(current_count / total_count * 100, current_count, total_count))
        f.write("Initial timestamp: {0}\n".format(initial_timestamp))
        f.write("Final timestamp: {0}\n".format(current_timestamp))
        f.write("Execution time: {0} hours, {1} minutes, {2} seconds. \n".format(time_difference.seconds // 3600, (time_difference.seconds % 3600) // 60, time_difference.seconds % 60))                                                                 
                

def count_cases(folder):
    """
    Count the number of files in a folder
    """
    global total_count
    total_count = len(os.listdir(folder))


def assign_to_thread(script_path):
    """
    Assign a given script to a runner
    """
    global slots, semaphore
    index = get_available_slot(slots)
    if index == -1:
        logging.error("Trying to assign when no threads are available")
        exit()
    slots[index] = False
    threading.Thread(target=consumer_thread, args=(script_path, configuration.packetdrill_command, configuration.target_command, index)).start()
    

def consumer_thread(script, packetdrill_command, target_command, index):
    """
    Thread to process a single script
    """
    global slots, semaphore
    envs = {
        interface_name_env: configuration.interface_placeholder.format(index  + configuration.interface_index_offset)
    }
    logging.info("Executing script '{0}' {1}".format(script, index))
    target_output_file = open(os.path.join(configuration.log_directory, os.path.basename(script) + target_trace_suffix,), "w")
    packetdrill_output_file = open(os.path.join(configuration.log_directory, os.path.basename(script) + packetdrill_trace_suffix,), "w")
    target_process = subprocess.Popen(target_command, env=envs, stdout=target_output_file, stderr=target_output_file)
    hang = False
    crash = False
    try:
        command = copy.deepcopy(packetdrill_command)
        command.append(script)
        subprocess.run(command, env=envs, timeout=target_timeout, stdout=packetdrill_output_file, stderr=packetdrill_output_file)
        time.sleep(target_timeout / 2)
    except subprocess.TimeoutExpired:
        logging.error("Timeout in packetdrill for file '{0}'".format(script))
        hang = True
        if target_process.poll() is not None:
            crash = True
            log_file(script)
        else:
            log_file(script, is_hang=True)
    finally:
        if target_process.poll() is not None and hang is False:
            log_file(script)
            crash = True
        if target_process.poll() is None:
            target_process.terminate()
            try:
                target_process.wait(timeout=target_timeout)
            except subprocess.TimeoutExpired:
                target_process.kill()
                target_process.wait()
        target_output_file.close()
        packetdrill_output_file.close()
        if not crash:
            os.remove(target_output_file.name)
            os.remove(packetdrill_output_file.name)    
        slots[index] = True 
        os.remove(script)
        semaphore.release()


def init_slots():
    """
    Initialize the slots dict
    """
    slots = {}
    for i in range(configuration.number_runners):
        slots[i] = True
    return slots


def get_available_slot(slots):
    """
    Get the first available slot
    """
    index = -1
    for i in range(configuration.number_runners):
        if slots.get(i):
            index = i
            break
    return index


def log_file(script, is_hang=False):
    """
    Log the script to a file
    """
    message = ""
    path = None
    if is_hang:
        message = "Hang on script '{0}'. "
        path = configuration.hanging_directory
    else:
        message = "Crash on script '{0}'. "
        path = configuration.crashing_directory
    logging.debug(message.format(script))
    shutil.copy(script, os.path.join(os.path.abspath(path), os.path.basename(script)))



def increasing_indexes(indexes):
    """
    Check if a list of indexes are increasing
    """
    for i in range(len(indexes) - 1):
        if indexes[i] >= indexes[i + 1]:
            return False
    return True



