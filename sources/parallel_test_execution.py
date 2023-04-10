""" Parallel test execution functions """

# System
import logging
import threading
import os

# Script generator
import sources.generate_scripts
import configuration


# Variables
semaphore = threading.Semaphore(configuration.number_runners)
slots = {}

def execute_and_generate_test(test_cases, templates_filenames, folder, packetdrill_command, target_command):
    sources.generate_scripts.remove_scripts()
    templates = sources.generate_scripts.preload_templates(templates_filenames)
    for test_case in test_cases:
        single_cases = sources.generate_scripts.create_individual_cases(test_case)
        for index, case in enumerate(single_cases):
            script_cases = sources.generate_scripts.generate_case(case, test_case["name"], templates, index)
            for script in script_cases:
                script_path = os.path.join(configuration.generated_folder, script)
                with open(script_path, "w") as script_file:
                    script_file.write(script_cases[script])
                logging.debug("script file '{0}' written".format(script))
                assign_to_thread(script_path)
                

def assign_to_thread():
    pass
