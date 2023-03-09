""" Main script to generate test cases and run """

# Test cases
from test_cases import test_cases

# Generate scripts
from generate_scripts import generate_scripts

# Execute tests
from execute_test import execute_test


# Constants
templates_filenames = [
    'templates/fuzz-template-tcp-established-option.pkt',
    'templates/fuzz-template-tcp-established.pkt',
    'templates/fuzz-template-tcp-fin-wait.pkt',
    'templates/fuzz-template-tcp-last-ack.pkt',
    'templates/fuzz-template-tcp-listen.pkt',
    'templates/fuzz-template-tcp-send.pkt', # LWIP fails with this file
    'templates/fuzz-template-tcp-syn-rcvd.pkt',
    'templates/fuzz-template-tcp-syn-sent.pkt',
]

generated_folder = 'scripts/'

packetdrill_command = 'sudo /home/rcalvome/Documents/app/packetdrill/gtests/net/packetdrill/packetdrill --so_filename=/home/rcalvome/Documents/app/rtos-bridge/libfreertos-bridge.so --fm_filename=/home/rcalvome/Documents/app/packet-mutation/libmutation-interface.so --local_ip=125.0.75.1 --remote_ip=125.0.75.5 --verbose --non_fatal=packet --tolerance_usec=1000000 {0}'

#target = 'sudo /home/rcalvome/Documents/app/lwip/build/contrib/ports/unix/example_app/example_app'
target = 'sudo /home/rcalvome/Documents/app/FreeRTOS/FreeRTOS-Plus/Demo/FreeRTOS_Plus_TCP_Echo_Posix/build/posix_demo'


def main():
    # Generate Packetdrill script from test cases file
    generate_scripts(test_cases, templates_filenames)
    # Excecute tests
    execute_test(generated_folder, packetdrill_command, target)
    # Generate stats of performance
    #stats()


if __name__ == "__main__":
    main()