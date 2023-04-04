#!/usr/bin/python3
""" Main script of Script generator """

# System
import logging
import getopt
import sys

# Configuration
import configuration
from test_cases import test_cases

# Script generator
from sources.generate_scripts import generate_scripts
from sources.execute_test import execute_test
from sources.producer_consumer_execution import generate_execute_async
from sources.plot_stats import plot_stats
from sources.clean_resources import clean_resources


def main(generate, execute, stats, clean):
    """
    Main execution function. start the processes
    """
    if clean:
        clean_resources()
        exit()
    if generate and execute:
        generate_execute_async(test_cases, configuration.templates_filenames, configuration.generated_folder, configuration.packetdrill_command, configuration.target_command)
    if generate and not execute:
        generate_scripts(test_cases, configuration.templates_filenames)
    if not generate and execute: 
        execute_test(configuration.generated_folder, configuration.packetdrill_command, configuration.target_command, generate)
    if stats: #TODO: Evaluate stats
        plot_stats()


if __name__ == '__main__':
    """
    Main execution. Execute taking command line args
    """
    generate = False
    execute = False
    stats = False
    clean = False
    argument_list = sys.argv[1:]
    options = 'ges'
    long_options = ['generate', 'execute', 'stats', 'verbose', 'clean']
    try:
        debug = False
        arguments, values = getopt.getopt(argument_list, options, long_options)
        for current_argument, current_value in arguments:
            if current_argument in ('-g', '--generate'):
                generate = True
            elif current_argument in ('-e', '--execute'):
                execute = True
            elif current_argument in ('-s', '--stats'):
                stats = True
            elif current_argument in ('--verbose'):
                debug = True
            elif current_argument in ('--clean'):
                clean = True
        logging.basicConfig(format="%(message)s", level=logging.DEBUG if debug else logging.INFO)
        main(generate, execute, stats, clean)
    except getopt.error as err:
        logging.error(err)