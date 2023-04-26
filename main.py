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
from sources.parallel_test_execution import execute_and_generate_test
from sources.plot_stats import plot_stats
from sources.clean_resources import clean_resources
from sources.trace_deduplication import trace_deduplication


def main(generate, execute, stats, clean, deduplicate):
    """
    Main execution function. start the processes
    """
    if clean:
        clean_resources()
    if generate and execute:
        execute_and_generate_test()
    if generate and not execute:
        generate_scripts(test_cases, configuration.templates_filenames)
    if not generate and execute:
        pass
#        execute_test(configuration.generated_folder, configuration.packetdrill_command, configuration.target_command, generate)
    if deduplicate:
        trace_deduplication()
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
    deduplicate = False
    argument_list = sys.argv[1:]
    options = 'gesd'
    long_options = ['generate', 'execute', 'stats', 'verbose', 'clean', 'deduplicate']
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
            elif current_argument in ('-d', '--deduplicate'):
                deduplicate = True
        logging.basicConfig(format="%(message)s", level=logging.DEBUG if debug else logging.INFO)
        main(generate, execute, stats, clean, deduplicate)
    except getopt.error as err:
        logging.error(err)
