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


def execute_test(folder, command, target, generate):
    """
    Execute script test using the target and packetdrill
    """
    global target_process
    signal.signal(signal.SIGINT, sigint_handler)
    if generate:
        watch_manager = pyinotify.WatchManager()
        watch_manager.add_watch(folder, pyinotify.IN_CREATE, auto_add=True)
        notifier = pyinotify.Notifier(watch_manager, EventHandler())
        notifier.loop()
    else:
        scripts = [os.path.abspath(os.path.join(folder, f)) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        for script in scripts:
            process_script(script, command, target)
        if target_process is not None and target_process.poll() is None:
            target_process.kill()


def process_script(script, packetdrill_command, target_command):
    """
    Process a single script
    """
    global target_process
    logging.debug("Executing script '{0}'".format(script))
    hang = False
    if target_process is None or target_process.poll() is not None:
        target_process = subprocess.Popen(target_command, env={'TAP_INTERFACE_NAME': 'tun0'})
        logging.debug("Target started")
    try:
        command = copy.deepcopy(packetdrill_command)
        command.append(script)
        print("Command: ", " ".join(command))
        subprocess.run(command, env={'TAP_INTERFACE_NAME': 'tun0'}, timeout=2)
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
