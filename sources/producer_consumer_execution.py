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
consumer_available_event = threading.Event()
slots = {}


def generate_execute_async(test_cases, templates_filenames, folder, packetdrill_command, target_command):
    """
    Generate and execute test cases using multiple runners
    """
    global generation_ended, slots
    sources.generate_scripts.remove_scripts()
    p_thread = threading.Thread(target=producer_thread, args=(test_cases, templates_filenames))
    p_thread.start()
    for i in range(configuration.number_runners):
        slots[i] = True
    while not generation_ended:
        consumer_available_event.set()
        scripts = [os.path.abspath(os.path.join(folder, f)) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        if len(scripts) == 0:
            continue
        semaphore.acquire()
        script = shutil.move(scripts[0], configuration.processing_directory)
        index = -1
        for i in range(configuration.number_runners):
            if slots.get(i):
                index = i
                break
        slots[i] = False
        c_thread = threading.Thread(target=consumer_thread, args=(str(script), packetdrill_command, target_command, semaphore, index))
        c_thread.start()


def producer_thread(test_cases, templates_filenames):
    """
    Thread to produce test scripts
    """
    global consumer_available_event, generation_ended
    templates = sources.generate_scripts.preload_templates(templates_filenames)
    for test_case in test_cases:
        single_cases = sources.generate_scripts.create_individual_cases(test_case)
        for index, case in enumerate(single_cases):
            script_cases = sources.generate_scripts.generate_case(case, test_case["name"], templates, index)
            for script in script_cases:
                consumer_available_event.wait()
                with open(os.path.join(configuration.generated_folder, script), "w") as script_file:
                    script_file.write(script_cases[script])
                logging.debug("script file '{0}' written".format(script))
                consumer_available_event.clear()
    generation_ended = True


def consumer_thread(script, packetdrill_command, target_command, semaphore, index):
    """
    Thread to process a single script
    """
    global slots
    logging.debug("Executing script '{0}' {1}".format(script, index))
    envs = {'TAP_INTERFACE_NAME': 'tap{0}'.format(index)}
    target_process = subprocess.Popen(target_command, env=envs)#, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    hang = False
    try:
        command = copy.deepcopy(packetdrill_command)
        command.append(script)
        subprocess.run(command, env=envs, timeout=2)#, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        logging.error("Timeout in packetdrill for file '{0}'".format(script))
        hang = True
        if target_process.poll() is not None:
            logging.debug("Crash on script '{0}'. ".format(script))
            shutil.copy(script, os.path.join(os.path.abspath(configuration.crashing_directory), os.path.basename(script)))
        else:
            logging.debug("Hang on script '{0}'. ".format(script))
            shutil.copy(script, os.path.join(os.path.abspath(configuration.hanging_directory), os.path.basename(script)))
    finally:
        time.sleep(2)
        if target_process.poll() is not None and hang is False:
            logging.debug("Crash on script '{0}'. ".format(script))
            shutil.copy(script, os.path.join(os.path.abspath(configuration.crashing_directory), os.path.basename(script)))
        if target_process.poll() is None:
            target_process.kill()           
            time.sleep(2)
        semaphore.release()
        slots[index] = True 
        os.remove(script)
