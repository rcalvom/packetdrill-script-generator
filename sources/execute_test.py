""" Functions to execute Packetdrill """

# System
import subprocess
import pyinotify
import threading
import logging
import shutil
import signal
import copy
import time
import os

# Script Generator
import configuration


# Variables
target_process = None


def execute_test_async(folder, packetdrill_command, target_command, runner_available_event, generation_ended_event):
    """
    Execute script test using the target and packetdrill asynchronously
    """
    semaphore = threading.Semaphore(configuration.number_runners)
    slots = ThreadSafeDict()
    for i in range(configuration.number_runners):
        slots.set(i, True)
    while not generation_ended_event.is_set():
        semaphore.acquire()
        runner_available_event.set()
        scripts = []
        while len(scripts) == 0 and not generation_ended_event.is_set():
            scripts = [os.path.abspath(os.path.join(folder, f)) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        index = -1
        for i in range(configuration.number_runners):
            if slots.get(i):
                index = i
                break
        if len(scripts) == 0:
            break
        thread = threading.Thread(target=process_script_thread, args=(scripts[0], packetdrill_command, target_command, semaphore, index))
        thread.start()


def execute_test(folder, command, target):
    """
    Execute script test using the target and packetdrill
    """
    global target_process
    signal.signal(signal.SIGINT, sigint_handler)
    scripts = [os.path.abspath(os.path.join(folder, f)) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    for script in scripts:
        process_script(script, command, target)
    if target_process is not None and target_process.poll() is None:
        target_process.kill()


def process_script_thread(script, packetdrill_command, target_command, semaphore, index):
    """
    Thread to process a single script
    """
    logging.debug("Executing script '{0}'".format(script))
    envs = {'TAP_INTERFACE_NAME': 'tap{0}'.format(index)}
    target_process = subprocess.Popen(target_command, env=envs, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    hang = False
    try:
        command = copy.deepcopy(packetdrill_command)
        command.append(script)
        subprocess.run(command, env=envs, timeout=2, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        logging.error("Timeout in packetdrill for file '{0}'".format(script))
        hang = True
        if target_process.poll() is not None:
            shutil.copy(script, os.path.join(os.path.abspath(configuration.crashing_directory), os.path.basename(script)))
        else:
            shutil.copy(script, os.path.join(os.path.abspath(configuration.hanging_directory), os.path.basename(script)))
    finally:
        time.sleep(1)
        if target_process.poll() is not None and hang is False:
            shutil.copy(script, os.path.join(os.path.abspath(configuration.crashing_directory), os.path.basename(script)))
        if target_process.poll() is None:
            target_process.kill()           
        os.remove(script)
        semaphore.release()

    

def process_script(script, packetdrill_command, target_command):
    """
    Process a single script
    """
    global target_process
    logging.debug("Executing script '{0}'".format(script))
    hang = False
    if target_process is None or target_process.poll() is not None:
        target_process = subprocess.Popen(target_command, env={'TAP_INTERFACE_NAME': 'tap0'})
        logging.debug("Target started")
    try:
        command = copy.deepcopy(packetdrill_command)
        command.append(script)
        print("Command: ", " ".join(command))
        subprocess.run(command, env={'TAP_INTERFACE_NAME': 'tap0'}, timeout=2)
    except subprocess.TimeoutExpired as exception:
        logging.error("Timeout in packetdrill for file '{0}'".format(script))
        hang = True
        if target_process.poll() is not None:
            shutil.copy(script, os.path.join(os.path.abspath(configuration.crashing_directory), os.path.basename(script)))
        else:
            target_process.kill()
            time.sleep(1)
            shutil.copy(script, os.path.join(os.path.abspath(configuration.hanging_directory), os.path.basename(script)))
    except Exception as exception:
        logging.error(exception)
        exit()
    if target_process.poll() is not None and hang is False:
        logging.debug("Target process stopped. Writing input")
        shutil.copy(script, os.path.join(os.path.abspath(configuration.crashing_directory), os.path.basename(script)))
    if target_process.poll() is not None:
        time.sleep(2)
    os.remove(script)

    

def sigint_handler(signal, frame):
    """
    Callback for Ctrl+C command
    """
    logging.log("Interrupting Execution...")
    logging.log("Ctrl+C pressed. Signalling all threads to stop...")
    exit()


class EventHandler(pyinotify.ProcessEvent):
    """
    Class to define the event handler
    """
    def process_IN_CREATE(self, event):
        """
        This method is called when a new file is created in the directory
        """
        # Logica para cada lanzar runners
        pass


class ThreadSafeDict():
    
    def __init__(self):
        """
        Constructor
        """
        self._dict = {}
        self._lock = threading.Lock()
 

    def get(self, key):
        """
        get an element of the dict
        """
        with self._lock:
            return self._dict[key]
        

    def set(self, key, value):
        """
        Set an element of the dict
        """
        with self._lock:
            self._dict[key] = value
 
    def length(self):
        """
        Return the length of the dict
        """
        with self._lock:
            return len(self._dict)