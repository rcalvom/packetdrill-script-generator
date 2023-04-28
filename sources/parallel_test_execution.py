""" Parallel test execution functions """

# System
import threading
import subprocess
import datetime
import logging
import shutil
import select
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
target_slots = []


def recursive_generation(indexes: list):
    global count, total_count, current_count, templates, semaphore
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
                    count += 1
                    if count < configuration.start_test_count:
                        continue
                    if count >= configuration.end_test_count:
                        continue
                    current_count += 1
                    if current_count % 100 == 0:
                        with open("stats.log", "w+") as f:
                            current_timestamp = datetime.datetime.fromtimestamp(time.time())
                            time_difference = current_timestamp - initial_timestamp
                            f.write("Total count: {0}\n".format(total_count))
                            f.write("Current count: {0}\n".format(current_count))
                            f.write("Progress: {0:.2f} ({1} / {2})%\n".format(current_count / total_count * 100, current_count, total_count))
                            f.write("Initial timestamp: {0}\n".format(initial_timestamp))
                            f.write("Current timestamp: {0}\n".format(current_timestamp))
                            f.write("Executing time: {0} hours, {1} minutes, {2} seconds. \n".format(time_difference.seconds // 3600, (time_difference.seconds % 3600) // 60, time_difference.seconds % 60))
                    script_path = os.path.join(configuration.generated_folder, script)
                    with open(script_path, "w") as script_file:
                      script_file.write(script_cases[script])
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
    global count, total_count, slots, initial_timestamp, target_slots
    initial_timestamp = datetime.datetime.fromtimestamp(time.time())
    slots = init_slots()
    target_slots = init_target_slots()
    count_cases([])
    sources.generate_scripts.remove_scripts()
    recursive_generation([]) 
    kill_all_targets()
    logging.info("Script generator: {0} test files have been written successfully".format(count))                                                                      
                

def count_cases(indexes: list):
    global total_count
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
            single_cases = sources.generate_scripts.create_individual_cases(test_case)
            for index, case in enumerate(single_cases):
                script_cases = sources.generate_scripts.generate_case(case, test_case["name"], templates, index)
                for _ in script_cases:
                    if total_count < configuration.start_test_count:
                        continue
                    if total_count >= configuration.end_test_count:
                        continue
                    total_count += 1
    else:
        for index, test_case in enumerate(test_cases):
            new_indexes = copy.deepcopy(indexes)
            new_indexes.append(index)
            count_cases(new_indexes)


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
    global slots, target_slots, semaphore
    logging.info("Executing script '{0}' {1}".format(script, index))
    envs = {
        interface_name_env: configuration.interface_placeholder.format(index  + configuration.interface_index_offset)
    }
    if target_slots[index] is None or target_slots[index].poll() is not None:
        pipe = subprocess.PIPE
        target_slots[index] = subprocess.Popen(target_command, env=envs, stdout=pipe, stderr=pipe)
    hang = False
    crash = False
    try:
        command = copy.deepcopy(packetdrill_command)
        command.append(script)
        subprocess.run(command, env=envs, timeout=target_timeout, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(target_timeout / 2)
    except subprocess.TimeoutExpired:
        logging.error("Timeout in packetdrill for file '{0}'".format(script))
        hang = True
        if target_slots[index].poll() is not None:
            crash = True
            log_file(index, script)
        else:
            log_file(index, script, is_hang=True)
    finally:
        if target_slots[index].poll() is not None and hang is False:
            crash = True
            log_file(index, script)
        if not crash:
            os.path.join(configuration.log_directory, os.path.basename(script) + target_trace_suffix)
        slots[index] = True 
        os.remove(script)
        if hang:
            target_slots[index].kill()
        while select.select([target_slots[index].stdout], [], [], 0)[0]:
            line = target_slots[index].stdout.readline()
            if line == b'':
                break
        while select.select([target_slots[index].stderr], [], [], 0)[0]:
            line = target_slots[index].stderr.readline()
            if line == b'':
                break
        semaphore.release()


def init_slots():
    """
    Initialize the slots dict
    """
    slots = {}
    for i in range(configuration.number_runners):
        slots[i] = True
    return slots


def init_target_slots():
    """
    Initialize the targe slots dict
    """
    slots = []
    for i in range(configuration.number_runners):
        slots.append(None)
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


def log_file(index, script, is_hang=False):
    """
    Log the script to a file
    """
    global target_slots
    message = ""
    path = None
    if is_hang:
        message = "Hang on script '{0}'. "
        path = configuration.hanging_directory
    else:
        message = "Crash on script '{0}'. "
        path = configuration.crashing_directory
        file = open(os.path.join(configuration.log_directory, os.path.basename(script) + target_trace_suffix), "w")
        target_slots[index].stdout.flush()
        for line in target_slots[index].stdout: 
            file.write(line.decode('utf-8'))
        target_slots[index].stderr.flush()
        for line in target_slots[index].stderr: 
            file.write(line.decode('utf-8'))
        file.flush()
        file.close()
    logging.debug(message.format(script))
    shutil.copy(script, os.path.join(os.path.abspath(path), os.path.basename(script)))


def kill_all_targets():
    """ 
    Kill all the targets 
    """
    global target_slots
    for target in target_slots:
        #if target.poll() is None:
        
            print("Target ", target)
            target.kill()


def increasing_indexes(indexes):
    """
    Check if a list of indexes are increasing
    """
    for i in range(len(indexes) - 1):
        if indexes[i] >= indexes[i + 1]:
            return False
    return True



