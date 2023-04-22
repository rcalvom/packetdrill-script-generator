""" Configuration file for lwIP"""

# Packetdrill command (IPv4)
# Oneline script: sudo TAP_INTERFACE_NAME=tap0 /home/rcalvome/Documents/app/packetdrill/gtests/net/packetdrill/packetdrill --so_filename=/home/rcalvome/Documents/app/rtos-bridge/libfreertos-bridge.so --fm_filename=/home/rcalvome/Documents/app/packet-mutation/libmutation-interface.so --local_ip=125.0.75.1 --remote_ip=125.0.75.5 --verbose --non_fatal=packet --tolerance_usec=1000000 /home/rcalvome/Documents/app/packetdrill-script-generator/test.pkt 
packetdrill_command =   [
                            '/home/rcalvome/Documents/app/packetdrill/gtests/net/packetdrill/packetdrill',
                            '--so_filename=/home/rcalvome/Documents/app/rtos-bridge/libfreertos-bridge.so',
                            '--fm_filename=/home/rcalvome/Documents/app/packet-mutation/libmutation-interface.so',
                            '--local_ip=125.0.75.1',
                            '--remote_ip=125.0.75.5',
                            '--verbose',
                            '--non_fatal=packet',
                            '--tolerance_usec=1000000'
                        ]

# Packetdrill command (IPv6)
# Oneline script: sudo TAP_INTERFACE_NAME=tap0 /home/rcalvome/Documents/app/packetdrill/gtests/net/packetdrill/packetdrill --so_filename=/home/rcalvome/Documents/app/rtos-bridge/libfreertos-bridge.so --fm_filename=/home/rcalvome/Documents/app/packet-mutation/libmutation-interface.so --local_ip=fe80::2801:f0ff:fec3:62d4 --remote_ip=fe80::2801:f0ff:fec3:62d5 --verbose --non_fatal=packet --ip_version=ipv6 --tolerance_usec=1000000 /home/rcalvome/Documents/app/packetdrill-script-generator/test.pkt
packetdrill_command =   [
                            '/home/rcalvome/Documents/app/packetdrill/gtests/net/packetdrill/packetdrill',
                            '--so_filename=/home/rcalvome/Documents/app/rtos-bridge/libfreertos-bridge.so',
                            '--fm_filename=/home/rcalvome/Documents/app/packet-mutation/libmutation-interface.so',
                            '--local_ip=fe80::2801:f0ff:fec3:62d4',
                            '--remote_ip=fe80::2801:f0ff:fec3:62d5',
                            '--verbose',
                            '--non_fatal=packet',
                            '--ip_version=ipv6',
                            '--tolerance_usec=1000000'
                        ]


# Target command. command to execute target system
# sudo TAP_INTERFACE_NAME=tap0 /home/rcalvome/Documents/app/lwip/build/contrib/ports/unix/example_app/example_app
target_command =    [
                        '/home/rcalvome/Documents/app/lwip/build/contrib/ports/unix/example_app/example_app'
                    ]

# Interface placeholder
interface_placeholder = 'tap{0}'

# offset of the interface index
interface_index_offset = 0

# Base output directoty
output_directory = 'lwip'

# Directory to store crashes
crashing_directory = 'lwip/crashes'

# Directory to store hangings
hanging_directory = 'lwip/hangings'

# Directory to store log files with traces
log_directory = 'lwip/traces'

# Directory to store debugged traces
debugged_directory = 'lwip/debugged_traces'