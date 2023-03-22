""" Functions to execute Packetdrill """

# System
import subprocess
import threading
import logging
import os


def execute_target_thread(target, return_values):
    """
    Function to execute a thread with the target. Wait for completion
    """
    process = subprocess.Popen(args=target.split(" "))
    try:
        process.wait(1)
        return_values["target"] = process.returncode
    except subprocess.TimeoutExpired:
        logging.warn("Timeout in target.")
        process.kill()
        return_values["target"] = -1
        

def execute_packetdrill_thread(command, script, return_values):
    """
    Function to execute a thread with packetdrill. Wait for completion
    """
    process = subprocess.Popen(args=command.format(script).split(" "))
    try:
        process.wait(1)
        return_values["packetdrill"] = process.returncode
    except subprocess.TimeoutExpired:
        logging.warn("Timeout in packetdrill.")
        process.kill()
        return_values["packetdrill"] = -1


def execute_test(folder, command, target):
    return_values = {}
    scripts = [os.path.abspath(os.path.join(folder, f)) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    for script in scripts:
        target_thread = threading.Thread(target=execute_target_thread, args=(target, return_values, ))
        packetdrill_thread = threading.Thread(target=execute_packetdrill_thread, args=(command, script, return_values))
        target_thread.start()
        packetdrill_thread.start()
        target_thread.join()
        packetdrill_thread.join()
        print("Return target: ", return_values["target"])
        print("Return packetdrill: ", return_values["packetdrill"])
        if return_values["target"] != 0:
            with open("error_target.log", "a") as f:
                f.write(script + "\n")
            logging.error("Error in target")
        if return_values["packetdrill"] != 0:
            with open("error_packetdrill.log", "a") as f:
                f.write(script + "\n")
            logging.error("Error in packetdrill")
        if return_values["target"] == 0 and return_values["packetdrill"] == 0:
            with open("success.log", "a") as f:
                f.write(script + "\n")
            


    
