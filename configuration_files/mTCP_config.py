""" Configuration file for FreeRTOS"""

# Debug mode
debug = False

# Number of runners
number_runners = 10

# Directory to store crashes
crashing_directory = 'output/crashes'

# Directory to store hangings
hanging_directory = 'output/hangings'

# Directory to store processing files
processing_directory = 'output/processing'

# Destination folder of all generated scripts
generated_folder = 'scripts'

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

# Packetdrill command
packetdrill_command =   [
                            '/home/rcalvome/Documents/app/packetdrill/gtests/net/packetdrill/packetdrill',
                            '--so_filename=/home/rcalvome/Documents/app/rtos-bridge/libfreertos-bridge.so',
                            '--fm_filename=/home/rcalvome/Documents/app/packet-mutation/libmutation-interface.so',
                            '--local_ip=125.0.75.0',
                            '--remote_ip=125.0.75.20',
                            '--verbose',
                            '--non_fatal=packet',
                            '--tolerance_usec=1000000'
                        ]

# Target command. command to execute target system
target_command =    [
                        '/home/rcalvome/Documents/app/FreeRTOS/FreeRTOS-Plus/Demo/FreeRTOS_Plus_TCP_Echo_Posix/build/posix_demo'
                    ]

