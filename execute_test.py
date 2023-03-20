""" Functions to execute Packetdrill """

# System
import subprocess
import threading
import logging
import signal
import os

# Variables
return_packetdrill = 0
return_target = 0


def execute_target_thread(target):
    """
    Thread to execute a thread with the target. Wait for completion
    """
    process = subprocess.Popen(args=target.split(" "), shell=True)
    try:
        process.wait(1)
    except subprocess.TimeoutExpired:
        logging.warn("Timeout in execution.")
        os.killpg(os.getpgid(process.pid), signal.SIGTERM) 
    return_target = process.returncode
        

def execute_packetdrill_thread(command, script):
    """
    Thread to execute a thread with packetdrill. Wait for completion
    """
    process = subprocess.Popen(args=[command.format(script)], shell=True)
    print()
    try:
        process.wait(1)
    except subprocess.TimeoutExpired:
        logging.warn("Timeout in execution.")
        os.killpg(os.getpgid(process.pid), signal.SIGTERM) 
    return_packetdrill = process.returncode


def execute_test(folder, command, target):
    scripts = [os.path.abspath(os.path.join(folder, f)) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    for script in scripts:
        target_thread = threading.Thread(target=execute_target_thread, args=(target,))
        #packetdrill_thread = threading.Thread(target=execute_packetdrill_thread, args=(command, script))
        target_thread.start()
        #packetdrill_thread.start()
        target_thread.join()
        #packetdrill_thread.join()
        logging.info("Return target: ", return_target)
        logging.info("Return packetdrill: ", return_packetdrill)
        if return_target != 0:
            logging.error("Error in target")
        if return_packetdrill != 0:
            logging.error("Error in packetdrill")
            


    
