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

