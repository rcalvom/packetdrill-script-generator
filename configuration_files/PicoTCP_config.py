""" Configuration file for PicoTCP"""

# Packetdrill command (IPv4)
# Oneline script: sudo TAP_INTERFACE_NAME=tap0 /home/rcalvome/Documents/app/packetdrill/gtests/net/packetdrill/packetdrill --so_filename=/home/rcalvome/Documents/app/rtos-bridge/libfreertos-bridge.so --fm_filename=/home/rcalvome/Documents/app/packet-mutation/libmutation-interface.so --local_ip=192.168.5.4 --remote_ip=192.168.5.5 --bind_port=5678 --connect_port=8765 --is_anyip --verbose --non_fatal=packet --tolerance_usec=1000000 /home/rcalvome/Documents/app/packetdrill-script-generator/scripts/packetdrill_script_trun_tcp_1_5.pkt
packetdrill_command =   [
                            '/home/rcalvome/Documents/app/packetdrill/gtests/net/packetdrill/packetdrill',
                            '--so_filename=/home/rcalvome/Documents/app/rtos-bridge/libfreertos-bridge.so',
                            '--fm_filename=/home/rcalvome/Documents/app/packet-mutation/libmutation-interface.so',
                            '--local_ip=192.168.5.4',
                            '--remote_ip=192.168.5.5',
                            '--bind_port=5678',
                            '--connect_port=8765',
                            '--is_anyip',
                            '--verbose',
                            '--non_fatal=packet',
                            '--tolerance_usec=1000000'
                        ]

# Packetdrill command (IPv6)
# Oneline script: sudo TAP_INTERFACE_NAME=tap0 /home/rcalvome/Documents/app/packetdrill/gtests/net/packetdrill/packetdrill --so_filename=/home/rcalvome/Documents/app/rtos-bridge/libfreertos-bridge.so --fm_filename=/home/rcalvome/Documents/app/packet-mutation/libmutation-interface.so --local_ip=fc00::302:304:506:708 --remote_ip=fc00::302:304:506:706 --bind_port=5678 --connect_port=8765 --ip_version=ipv6 --is_anyip --verbose --non_fatal=packet --tolerance_usec=1000000 /home/rcalvome/Documents/app/packetdrill-script-generator/test.pkt
# packetdrill_command =   [
#                             '/home/rcalvome/Documents/app/packetdrill/gtests/net/packetdrill/packetdrill',
#                             '--so_filename=/home/rcalvome/Documents/app/rtos-bridge/libfreertos-bridge.so',
#                             '--fm_filename=/home/rcalvome/Documents/app/packet-mutation/libmutation-interface.so',
#                             '--local_ip=fc00::302:304:506:708',
#                             '--remote_ip=fc00::302:304:506:706',
#                             '--bind_port=5678',
#                             '--connect_port=8765',
#                             '--ip_version=ipv6',
#                             '--is_anyip',
#                             '--verbose',
#                             '--non_fatal=packet',
#                             '--tolerance_usec=1000000'
#                         ]

# Target command. command to execute target system
#sudo TAP_INTERFACE_NAME=tap0 /home/rcalvome/Documents/app/picotcp/build/pd_fuzz/fuzz-agent.elf 
target_command =    [
                        '/home/rcalvome/Documents/app/picotcp/build/pd_fuzz/fuzz-agent.elf'
                    ]

# Interface placeholder
interface_placeholder = 'tap{0}'

# offset of the interface index
interface_index_offset = 0

# Start test count
start_test_count = 0

# End test count
end_test_count = 99999999

# Base output directoty
output_directory = 'pico'

# Directory to store crashes
crashing_directory = 'pico/crashes'

# Directory to store hangings
hanging_directory = 'pico/hangings'

# Directory to store log files with traces
log_directory = 'pico/traces'

# Directory to store debugged traces
debugged_directory = 'pico/debugged_traces'