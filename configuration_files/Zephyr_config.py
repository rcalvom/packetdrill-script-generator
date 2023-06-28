""" Configuration file for Zephyr"""

# Packetdrill command (IPv4)
# Oneline script: sudo TAP_INTERFACE_NAME=tap0 /home/rcalvome/Documents/app/packetdrill/gtests/net/packetdrill/packetdrill --so_filename=/home/rcalvome/Documents/app/rtos-bridge/libfreertos-bridge.so --fm_filename=/home/rcalvome/Documents/app/packet-mutation/libmutation-interface.so --local_ip=192.0.2.1 --remote_ip=192.0.2.2 --bind_port=4242 --connect_port=8765 --is_anyip --verbose --non_fatal=packet --tolerance_usec=1000000 /home/rcalvome/Documents/app/packetdrill-script-generator/vulnerabilities/Contiki/packetdrill_script_data_offset_0_1.pkt
packetdrill_command =   [
                            '/home/rcalvome/Documents/app/packetdrill/gtests/net/packetdrill/packetdrill',
                            '--so_filename=/home/rcalvome/Documents/app/rtos-bridge/libfreertos-bridge.so',
                            '--fm_filename=/home/rcalvome/Documents/app/packet-mutation/libmutation-interface.so',
                            '--local_ip=192.0.2.1',
                            '--remote_ip=192.0.2.2',
                            '--bind_port=4242',
                            '--connect_port=8765',
                            '--is_anyip',
                            '--verbose',
                            '--non_fatal=packet',
                            '--tolerance_usec=1000000'
                        ]

# Target command. command to execute target system
#sudo TAP_INTERFACE_NAME=tap0 /home/rcalvome/Documents/app/picotcp/build/pd_fuzz/fuzz-agent.elf 
target_command =    [
                        '/home/rcalvome/Documents/app/zephyrproject/build/zephyr/zephyr.elf'
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
output_directory = 'zephyr'

# Directory to store crashes
crashing_directory = 'zephyr/crashes'

# Directory to store hangings
hanging_directory = 'zephyr/hangings'

# Directory to store log files with traces
log_directory = 'zephyr/traces'

# Directory to store debugged traces
debugged_directory = 'zephyr/debugged_traces'