""" Configuration file for FreeRTOS"""

# Packetdrill command (IPv4)
# sudo TAP_INTERFACE_NAME=tap0 /home/rcalvome/Documents/app/packetdrill/gtests/net/packetdrill/packetdrill --so_filename=/home/rcalvome/Documents/app/rtos-bridge/libfreertos-bridge.so --fm_filename=/home/rcalvome/Documents/app/packet-mutation/libmutation-interface.so --local_ip=125.0.75.0 --remote_ip=125.0.75.20 --bind_port=5678 --connect_port=8765 --is_anyip --verbose --non_fatal=packet --tolerance_usec=1000000 /home/rcalvome/Documents/app/packetdrill-script-generator/test.pkt
packetdrill_command =   [
                            '/home/rcalvome/Documents/app/packetdrill/gtests/net/packetdrill/packetdrill',
                            '--so_filename=/home/rcalvome/Documents/app/rtos-bridge/libfreertos-bridge.so',
                            '--fm_filename=/home/rcalvome/Documents/app/packet-mutation/libmutation-interface.so',
                            '--local_ip=125.0.75.0',
                            '--remote_ip=125.0.75.20',
                            '--bind_port=5678', 
                            '--connect_port=8765', 
                            '--is_anyip',
                            '--verbose',
                            '--non_fatal=packet',
                            '--tolerance_usec=1000000'
                        ]

# Target command. command to execute target system
# sudo TAP_INTERFACE_NAME=tap0 /home/rcalvome/Documents/app/FreeRTOS/FreeRTOS-Plus/Demo/FreeRTOS_Plus_TCP_Echo_Posix/build/posix_demo
target_command =    [
                        '/home/rcalvome/Documents/app/FreeRTOS/FreeRTOS-Plus/Demo/FreeRTOS_Plus_TCP_Echo_Posix/build/posix_demo'
                    ]

# Interface placeholder
interface_placeholder = 'tap{0}'

# Offset of the interface index
interface_index_offset = 0

# Start test count
start_test_count = 0

# End test count
end_test_count = 99999999

# Base output directoty
output_directory = 'freertos'

# Directory to store crashes
crashing_directory = 'freertos/crashes'

# Directory to store hangings
hanging_directory = 'freertos/hangings'

# Directory to store log files with traces
log_directory = 'freertos/traces'

# Directory to store debugged traces
debugged_directory = 'freertos/debugged_traces'