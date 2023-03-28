""" Configuration file """

# Debug mode
debug = True

# Number of runners
number_runners = 3

# Directory to store crashes
crashing_directory = "output/crashes"

# Directory to store hangings
hanging_directory = "output/hangings"

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
]

# Packetdrill command (it must include a placeholder to script filename)
packetdrill_command =   [
                            '/home/pamusuo/research/ampaschal-packetdrill/gtests/net/packetdrill/packetdrill',
                            '--so_filename=/home/pamusuo/research/rtos-fuzzing/rtos-bridge/libfreertos-bridge.so',
                            '--fm_filename=/home/pamusuo/research/rtos-fuzzing/packet-mutation/libmutation-interface.so',
                            '--local_ip=125.0.75.0',
                            '--remote_ip=125.0.75.20',
                            '--bind_port=5678',
                            '--connect_port=8765',
                            '--verbose',
                            '--non_fatal=packet',
                            '--tolerance_usec=1000000'
                        ]

# Target command. command to execute target system
target_command =    [
                        '/home/rcalvome/Documents/app/FreeRTOS/FreeRTOS-Plus/Demo/FreeRTOS_Plus_TCP_Echo_Posix/build/posix_demo'
                    ]
