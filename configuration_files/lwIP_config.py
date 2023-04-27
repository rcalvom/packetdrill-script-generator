""" Configuration file for lwIP"""

# Packetdrill command (IPv4)
# Oneline script: sudo TAP_INTERFACE_NAME=tap0 /home/rcalvome/Documents/app/packetdrill/gtests/net/packetdrill/packetdrill --so_filename=/home/rcalvome/Documents/app/rtos-bridge/libfreertos-bridge.so --fm_filename=/home/rcalvome/Documents/app/packet-mutation/libmutation-interface.so --local_ip=125.0.75.1 --remote_ip=125.0.75.5 --bind_port=5678 --connect_port=8765 --is_anyip --verbose --non_fatal=packet --tolerance_usec=1000000 /home/rcalvome/Documents/app/packetdrill-script-generator/test.pkt
# packetdrill_command =   [
#                             '/home/rcalvome/Documents/app/packetdrill/gtests/net/packetdrill/packetdrill',
#                             '--so_filename=/home/rcalvome/Documents/app/rtos-bridge/libfreertos-bridge.so',
#                             '--fm_filename=/home/rcalvome/Documents/app/packet-mutation/libmutation-interface.so',
#                             '--local_ip=125.0.75.1',
#                             '--remote_ip=125.0.75.5',
#                             '--bind_port=5678', 
#                             '--connect_port=8765', 
#                             '--is_anyip',
#                             '--verbose',
#                             '--non_fatal=packet',
#                             '--tolerance_usec=1000000'
#                         ]

# Packetdrill command (IPv6)
# Oneline script: sudo TAP_INTERFACE_NAME=tap0 /home/rcalvome/Documents/app/packetdrill/gtests/net/packetdrill/packetdrill --so_filename=/home/rcalvome/Documents/app/rtos-bridge/libfreertos-bridge.so --fm_filename=/home/rcalvome/Documents/app/packet-mutation/libmutation-interface.so --local_ip=FE80::211:22FF:FE33:4441 --remote_ip=FE80::211:22FF:FE33:4442 --bind_port=5678 --connect_port=8765 --is_anyip --verbose --non_fatal=packet --ip_version=ipv6 --tolerance_usec=1000000 /home/rcalvome/Documents/app/packetdrill-script-generator/test.pkt
packetdrill_command =   [
                            '/home/rcalvome/Documents/app/packetdrill/gtests/net/packetdrill/packetdrill',
                            '--so_filename=/home/rcalvome/Documents/app/rtos-bridge/libfreertos-bridge.so',
                            '--fm_filename=/home/rcalvome/Documents/app/packet-mutation/libmutation-interface.so',
                            '--local_ip=FE80::211:22FF:FE33:4441',
                            '--remote_ip=FE80::211:22FF:FE33:4442',
                            '--bind_port=5678', 
                            '--connect_port=8765', 
                            '--is_anyip',
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

# Start test count
start_test_count = 0

# End test count
end_test_count = 999999999

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
