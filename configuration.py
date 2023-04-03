""" Configuration file """

# Script Generator (Uncomment only the corresponding to the system to test)
# from configuration_files.FreeRTOS_config import *
# from configuration_files.Contiki_config import *
from configuration_files.PicoTCP_config import *
# from configuration_files.lwIP_config import *
# from configuration_files.mTCP_config import *

# Number of runners
number_runners = 5

# Directory to store crashes
crashing_directory = 'output/crashes'

# Directory to store hangings
hanging_directory = 'output/hangings'

# Directory to store processing files
processing_directory = 'output/processing'

# Destination folder of all generated scripts
generated_folder = 'scripts/'

# List the template files to use
templates_filenames = [
    'templates/fuzz-template-tcp-established-option.pkt',
    'templates/fuzz-template-tcp-established.pkt',
    'templates/fuzz-template-tcp-fin-wait.pkt',
    'templates/fuzz-template-tcp-last-ack.pkt',
    'templates/fuzz-template-tcp-listen.pkt',
    'templates/fuzz-template-tcp-send.pkt',
    'templates/fuzz-template-tcp-syn-rcvd.pkt',
    'templates/fuzz-template-tcp-syn-sent.pkt',
    'templates/fuzz-template-tcp-y.pkt',
    'templates/fuzz-template-tcp-z.pkt'
]