""" Producer and consumer excecution """

# System
import subprocess
import threading
import logging
import shutil
import copy
import time
import os

# Script generator
import configuration
import sources.generate_scripts

generation_ended = False
semaphore = threading.Semaphore(configuration.number_runners)
script_required_event = threading.Event()
script_ready_event = threading.Event()
slots = {}


def generate_execute_async(test_cases, templates_filenames, folder, packetdrill_command, target_command):
    """
    Generate and execute test cases using multiple runners
    """
    global generation_ended, slots
    init_slots()
    p_thread = threading.Thread(target=producer_thread, args=(test_cases, templates_filenames))
    p_thread.start()
    while not generation_ended:
        semaphore.acquire()
        script_required_event.set()
        script_ready_event.wait()
        script_ready_event.clear()
        scripts = [os.path.abspath(os.path.join(folder, f)) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        script = shutil.move(scripts[0], configuration.processing_directory)
        index = get_available_slot()
        if index == -1:
            logging.error("Trying to assign when no threads are available")
            exit()
        slots[index] = False
        c_thread = threading.Thread(target=consumer_thread, args=(str(script), packetdrill_command, target_command, semaphore, index))
        c_thread.start()


def producer_thread(test_cases, templates_filenames):
    """
    Thread to produce test scripts
    """
    global script_required_event, generation_ended
    sources.generate_scripts.remove_scripts()
    templates = sources.generate_scripts.preload_templates(templates_filenames)
    for test_case in test_cases:
        single_cases = sources.generate_scripts.create_individual_cases(test_case)
        for index, case in enumerate(single_cases):
            script_cases = sources.generate_scripts.generate_case(case, test_case["name"], templates, index)
            for script in script_cases:
                script_required_event.wait()
                script_required_event.clear()
                with open(os.path.join(configuration.generated_folder, script), "w") as script_file:
                    script_file.write(script_cases[script])
                logging.debug("script file '{0}' written".format(script))
                script_ready_event.set()
    generation_ended = True


def consumer_thread(script, packetdrill_command, target_command, semaphore, index):
    """
    Thread to process a single script
    """
    global slots
    envs = {
        'TAP_INTERFACE_NAME': 'tun{0}'.format(index)
        }
    logging.debug("Executing script '{0}' {1}".format(script, index))
    target_output_file = open(os.path.join(configuration.log_directory, os.path.basename(script) + ".target.log",), "w")
    packetdrill_output_file = open(os.path.join(configuration.log_directory, os.path.basename(script) + ".packetdrill.log",), "w")
    target_process = subprocess.Popen(target_command, env=envs, stdout=target_output_file, stderr=target_output_file)#, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    hang = False
    crash = False
    try:
        command = copy.deepcopy(packetdrill_command)
        command.append(script)
        subprocess.run(command, env=envs, timeout=2, stdout=packetdrill_output_file, stderr=packetdrill_output_file)
    except subprocess.TimeoutExpired:
        logging.error("Timeout in packetdrill for file '{0}'".format(script))
        hang = True
        if target_process.poll() is not None:
            log_file(script)
        else:
            log_file(script, is_hang=True)
    finally:
        time.sleep(2)
        target_output_file.close()
        packetdrill_output_file.close()
        if target_process.poll() is not None and hang is False:
            log_file(script)
            crash = True
        if target_process.poll() is None:
            target_process.kill()           
            time.sleep(2)
        if not crash and not hang:
            os.remove(target_output_file.name)
            os.remove(packetdrill_output_file.name)    
        semaphore.release()
        slots[index] = True 
        os.remove(script)


def get_available_slot():
    global slots
    index = -1
    for i in range(configuration.number_runners):
        if slots.get(i):
            index = i
            break
    return index

def init_slots():
    global slots
    for i in range(configuration.number_runners):
        slots[i] = True
    

def log_file(script, is_hang=False):
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
