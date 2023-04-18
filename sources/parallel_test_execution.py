""" Parallel test execution functions """

# System
import threading
import subprocess
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
slots = {}


def recursive_generation(indexes: list):
    global count, templates, semaphore
    if len(indexes) == configuration.k:
        if not increasing_indexes(indexes):
            return
        else:
            test_case = {
                "name": "_X_".join([test_cases[x]["name"] for x in indexes]),
                "mutations": []
            }
            for index in indexes:
                test_case["mutations"] += test_cases[index]["mutations"]
            single_cases = sources.generate_scripts.create_individual_cases(test_case) #TODO Generate in another way this scripts (if k is big, it will load in memory lot of information)
            for index, case in enumerate(single_cases):
                script_cases = sources.generate_scripts.generate_case(case, test_case["name"], templates, index)
                for script in script_cases:
                    script_path = os.path.join(configuration.generated_folder, script)
                    with open(script_path, "w") as script_file:
                      script_file.write(script_cases[script])
                    count += 1
                    logging.info("script file '{0}' written".format(script))
                    semaphore.acquire()
                    assign_to_thread(script_path)
    else:
        for index, test_case in enumerate(test_cases):
            new_indexes = copy.deepcopy(indexes)
            new_indexes.append(index)
            recursive_generation(new_indexes)


def execute_and_generate_test():
    """
    Generate and execute at same time the tests
    """
    global count, slots
    slots = init_slots()
    sources.generate_scripts.remove_scripts()
    recursive_generation([]) 
    logging.info("Script generator: {0} test files have been written successfully".format(count))                                                                      
                

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
        if not hang and not crash:
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



