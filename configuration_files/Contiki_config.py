""" Configuration file for Contiki"""

# Packetdrill command
# sudo TAP_INTERFACE_NAME=tun0 /home/rcalvome/Documents/app/packetdrill/gtests/net/packetdrill/packetdrill --so_filename=/home/rcalvome/Documents/app/rtos-bridge/libfreertos-bridge.so --fm_filename=/home/rcalvome/Documents/app/packet-mutation/libmutation-interface.so --local_ip=fd00::302:304:506:708 --bind_port=5678 --connect_port=8765  --ip_version=ipv6 --verbose --non_fatal=packet --is_anyip --tolerance_usecs=1000000 /home/rcalvome/Documents/app/packetdrill-script-generator/scripts/packetdrill_script_source_port_0_0.pkt
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
# sudo TAP_INTERFACE_NAME=tun0 /home/rcalvome/Documents/app/contiki-ng/examples/fuzz-agent/udp-server.native
target_command =    [
                        '/home/rcalvome/Documents/app/contiki-ng/examples/fuzz-agent/udp-server.native'
                    ]

# Interface placeholder
interface_placeholder = 'tun{0}'

# offset of the interface index
interface_index_offset = 0

# Base output directoty
output_directory = 'contiki'

# Directory to store crashes
crashing_directory = 'contiki/crashes'

# Directory to store hangings
hanging_directory = 'contiki/hangings'

# Directory to store log files with traces
log_directory = 'contiki/traces'

# Directory to store debugged traces
debugged_directory = 'contiki/debugged_traces'

