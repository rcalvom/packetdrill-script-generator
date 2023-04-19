""" Trace deduplication """

# System
import logging
import shutil
import re
import os

# Script generator
import configuration


# Constants
original_file_regex = r"(^.+)\.(target|packetdrill)\.log"
is_asan_regex = r"ERROR: AddressSanitizer: (.*?) "
trace_line_regex = r"^ *#(\d+?) 0x.{12} in .+? .+/(.+?):(\d+)$"

crash_directory = "crashes"
hangs_directory = "hangs"
asan_directory = "crashes/asan"
unknown_directory = "crashes/unknown"


def trace_deduplication():
    """ 
    Remove the duplicate traces 
    """
    # Classify either crash or hang
    traces = os.listdir(configuration.log_directory)
    for trace in traces:
        classify_crashes_hangs(trace)

    # Classify crashes either unknown or ASAN
    debugged_crashes = os.listdir(os.path.join(configuration.debugged_directory, crash_directory))
    for trace in debugged_crashes:
        classify_crashes_types(trace)
    
    # Remove duplicated crashes by traces
    asan_types_folders = os.listdir(os.path.join(configuration.debugged_directory, asan_directory))
    for asan_type_folder in asan_types_folders:
       remove_duplicates(os.path.join(configuration.debugged_directory, asan_directory, asan_type_folder))
        

def classify_crashes_hangs(trace):
    """
    Classify a traces as either crash trace or hang trace
    """
    path_crash = os.path.join(configuration.crashing_directory, re.search(original_file_regex, trace).group(1))
    path_hang = os.path.join(configuration.hanging_directory, re.search(original_file_regex, trace).group(1))
    if os.path.isfile(path_crash):
        copy_file_to_path(
            os.path.join(configuration.log_directory, trace), 
            os.path.join(configuration.debugged_directory, crash_directory, trace)
        )
    elif os.path.isfile(path_hang):
        copy_file_to_path(
            os.path.join(configuration.log_directory, trace), 
            os.path.join(configuration.debugged_directory, hangs_directory, trace)
        )
    else:
        logging.error("The file '{0}' in the folder of traces does not correpond to neither a crash or a hang.")
        exit(-1)


def classify_crashes_types(trace):
    """
    Classify a crash trace as either ASAN trace or unknown trace
    """
    with open(os.path.join(configuration.debugged_directory, crash_directory, trace), "r") as file:
        flag = False
        for line in file:
            match = re.search(is_asan_regex, line)
            if match:
                flag = True
                error_type = match.group(1)
                move_file_to_path(os.path.join(configuration.debugged_directory, crash_directory, trace), os.path.join(configuration.debugged_directory, asan_directory, error_type, trace))
                break
        if not flag:
            move_file_to_path(os.path.join(configuration.debugged_directory, crash_directory, trace), os.path.join(configuration.debugged_directory, unknown_directory, trace))


def remove_duplicates(directory):
    """ 
    Remove duplicate crashes from a folder
    """
    traces_data = []
    traces = [os.path.join(directory, x) for x in os.listdir(directory)]
    for trace in traces:
        with open(trace, "r") as file: 
            for line in file:
                asan_trace = re.search(trace_line_regex, line)
                if asan_trace:
                    log_number = asan_trace.group(1) 
                    filename = asan_trace.group(2)
                    line_number = asan_trace.group(3)
                    data = [log_number, filename, line_number]
                    if data in traces_data:
                        os.remove(trace)
                        break
                        # duplicate
                    else:
                        traces_data.append(data)
                        break

                    
                    




def move_file_to_path(original_path, destination_path):
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    shutil.move(original_path, destination_path)
    logging.info("File '{}' moved to '{}'".format(original_path, destination_path))


def copy_file_to_path(original_path, destination_path):
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    shutil.copy(original_path, destination_path)
    logging.info("File '{}' copied to '{}'".format(original_path, destination_path))
