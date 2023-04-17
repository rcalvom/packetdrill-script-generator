""" Configuration file """

# Script Generator (Uncomment only the corresponding to the system to test)
# from configuration_files.FreeRTOS_config import *
from configuration_files.Contiki_config import *
# from configuration_files.PicoTCP_config import *
# from configuration_files.lwIP_config import *

# Number of test cases at same time
k = 2

# Number of runners
number_runners = 6

# Number of the initial interface
initial_interface = 18

# Base output directoty
output_directory = 'contiki_output'

# Directory to store crashes
crashing_directory = 'contiki_output/crashes'

# Directory to store hangings
hanging_directory = 'contiki_output/hangings'

# Directory to store log files with traces
log_directory = 'contiki_output/traces'

# Destination folder of all generated scripts
generated_folder = 'contiki_scripts/'

# List the template files to use
templates_filenames = [
    'templates/fuzz-template-tcp-established.pkt',
    'templates/fuzz-template-tcp-established-option.pkt',
    'templates/fuzz-template-tcp-fin-wait.pkt',
    'templates/fuzz-template-tcp-last-ack.pkt',
    'templates/fuzz-template-tcp-listen.pkt',
    'templates/fuzz-template-tcp-send.pkt',
    'templates/fuzz-template-tcp-syn-rcvd.pkt',
    'templates/fuzz-template-tcp-syn-sent.pkt'
]