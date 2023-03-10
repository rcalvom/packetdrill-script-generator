""" Main script to generate test cases and run """

# System
import getopt
import logging
import sys

# Configuration
import configuration
from test_cases import test_cases

# Script generator
from generate_scripts import generate_scripts
from execute_test import execute_test
from plot_stats import plot_stats


def main(generate, execute, stats):
    """
    Main execution function. start the processes
    """
    if generate:
        generate_scripts(test_cases, configuration.templates_filenames)
    if execute:
        execute_test(configuration.generated_folder, configuration.packetdrill_command, configuration.target_command)
    if stats:
        plot_stats()


if __name__ == '__main__':
    """
    Main execution. Execute taking command line args
    """
    generate = False
    execute = False
    stats = False
    argument_list = sys.argv[1:]
    options = 'ges'
    long_options = ['generate', 'execute', 'stats']
    logging.basicConfig(format="%(message)s")
    try:
        arguments, values = getopt.getopt(argument_list, options, long_options)
        for current_argument, current_value in arguments:
            if current_argument in ('-g', '--generate'):
                generate = True
            elif current_argument in ('-e', '--execute'):
                execute = True
            elif current_argument in ('-s', '--stats'):
                stats = True
        main(generate, execute, stats)
    except getopt.error as err:
        logging.error(err)