""" Configuration file """

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

# Destination folder of all generated scripts
generated_folder = 'scripts/'

# Packetdrill command (it must include a placeholder to script filename)
packetdrill_command =   (
                            'sudo /home/rcalvome/Documents/app/packetdrill/gtests/net/packetdrill/packetdrill '
                            '--so_filename=/home/rcalvome/Documents/app/rtos-bridge/libfreertos-bridge.so '
                            '--fm_filename=/home/rcalvome/Documents/app/packet-mutation/libmutation-interface.so '
                            '--local_ip=125.0.75.1 '
                            '--remote_ip=125.0.75.5 '
                            '--verbose '
                            '--non_fatal=packet '
                            '--tolerance_usec=1000000 '
                            '{0} '
                        )
# Target command. command to execute target system
target_command =    (
                        'sudo '
                        '/home/rcalvome/Documents/app/FreeRTOS/FreeRTOS-Plus/Demo/FreeRTOS_Plus_TCP_Echo_Posix/build/posix_demo '
                    )
