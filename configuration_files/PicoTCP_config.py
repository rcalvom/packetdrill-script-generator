""" Configuration file for PicoTCP"""

# Packetdrill command
# sudo TAP_INTERFACE_NAME=tap0 /home/rcalvome/Documents/app/packetdrill/gtests/net/packetdrill/packetdrill --so_filename=/home/rcalvome/Documents/app/rtos-bridge/libfreertos-bridge.so --fm_filename=/home/rcalvome/Documents/app/packet-mutation/libmutation-interface.so --local_ip=192.168.5.4 --remote_ip=192.168.5.5 --bind_port=5678 --connect_port=8765 --is_anyip --verbose --non_fatal=packet --tolerance_usec=1000000 /home/rcalvome/Documents/app/packetdrill-script-generator/scripts/packetdrill_script_trun_tcp_1_5.pkt
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

# Target command. command to execute target system
#sudo TAP_INTERFACE_NAME=tap0 /home/rcalvome/Documents/app/picotcp/build/pd_fuzz/fuzz-agent.elf 
target_command =    [
                        '/home/rcalvome/Documents/app/picotcp/build/pd_fuzz/fuzz-agent.elf'
                    ]

# Interface placeholder
interface_placeholder = 'tap{0}'

# offset of the interface index
interface_index_offset = 0

# Base output directoty
output_directory = 'picotcp'

# Directory to store crashes
crashing_directory = 'picotcp/crashes'

# Directory to store hangings
hanging_directory = 'picotcp/hangings'

# Directory to store log files with traces
log_directory = 'picotcp/traces'

# Directory to store debugged traces
debugged_directory = 'picotcp/debugged_traces'