#!/usr/bin/python3
""" Main script to generate test cases and run """

# System
import threading
import logging
import getopt
import sys

# Configuration
import configuration
from test_cases import test_cases

# Script generator
from generate_scripts import generate_scripts
from execute_test import execute_test
from producer_consumer_execution import generate_execute_async
from plot_stats import plot_stats


def main(generate, execute, stats):
    """
    Main execution function. start the processes
    """
    if generate and execute:
        generate_execute_async(test_cases, configuration.templates_filenames, configuration.generated_folder, configuration.packetdrill_command, configuration.target_command)
    if generate and not execute:
        generate_scripts(test_cases, configuration.templates_filenames)
    if not generate and execute: #TODO: Threading
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
    argument_list = sys.argv[1:]
    options = 'gesv'
    long_options = ['generate', 'execute', 'stats', 'verbose']
    try:
        arguments, values = getopt.getopt(argument_list, options, long_options)
        for current_argument, current_value in arguments:
            if current_argument in ('-g', '--generate'):
                generate = True
            elif current_argument in ('-e', '--execute'):
                execute = True
            elif current_argument in ('-s', '--stats'):
                stats = True
            elif current_argument in ('-v', '--verbose'):
                configuration.debug = True
        logging.basicConfig(format="%(message)s", level=logging.DEBUG if configuration.debug else None)
        main(generate, execute, stats)
    except getopt.error as err:
        logging.error(err)