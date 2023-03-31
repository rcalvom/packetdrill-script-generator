""" Configuration file for Contiki"""

# Debug mode
debug = False

# Number of runners
number_runners = 10

# Directory to store crashes
crashing_directory = 'output/crashes/'

# Directory to store hangings
hanging_directory = 'output/hangings/'

# Directory to store processing files
processing_directory = 'output/processing/'

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

# Packetdrill command
packetdrill_command =   [
                            '/home/rcalvome/Documents/app/packetdrill/gtests/net/packetdrill/packetdrill',
                            '--so_filename=/home/rcalvome/Documents/app/rtos-bridge/libfreertos-bridge.so',
                            '--fm_filename=/home/rcalvome/Documents/app/packet-mutation/libmutation-interface.so',
                            '--local_ip=fd00::302:304:506:708',
                            '--bind_port=5678',
                            '--connect_port=8765',
                            '--ip_version=ipv6',
                            '--is_anyip',
                            '--verbose',
                            '--non_fatal=packet',
                            '--tolerance_usec=1000000'
                        ]


# Target command. command to execute target system
target_command =    [
                        '/home/rcalvome/Documents/app/contiki-ng/examples/fuzz-agent/udp-server.native'
                    ]

