""" Functions to execute Packetdrill """

# System
import os

# Threading
import threading

# Pandas
#import pandas as pd


def execute_target(target):
    result = os.system(target)
    if result != 0:
        print("Target no 0")
    else:
        print("Target 0")


def execute_test(folder, command, target):
    scripts = [os.path.abspath(os.path.join(folder, f)) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    for script in scripts:
        #thread = threading.Thread(target=execute_target, args=(target,))
        #thread.start()
        print("Testing: ", script)
        return_value = os.system(command.format(script))
        if return_value != 0:
            print("script '{}' has errors\n".format(script))
            print("Packetdrill 1")
            #exit()
            with open("failure.txt", "a") as f:
                f.write(script + "\n")
            
        else:
            print("Packetdrill 0")
            with open("success.txt", "a") as f:
                f.write(script + "\n")
