""" Test Cases """

# Script Generator
from test_cases_files.test_cases_tcp import test_cases as tcp_tests
from test_cases_files.test_cases_udp import test_cases as udp_tests
from test_cases_files.test_cases_ipv4 import test_cases as ipv4_tests
from test_cases_files.test_cases_ipv6 import test_cases as ipv6_tests

# List of Test Cases
test_cases = []

# Select cases to test
test_cases += tcp_tests
# test_cases += udp_tests
test_cases += ipv4_tests
#test_cases += ipv6_tests