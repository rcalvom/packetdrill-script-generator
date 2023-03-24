""" Functions to generate Packetdrill scripts based on test cases list """

# System
import logging
import shutil
import copy
import os

# Inotify
from pyinotify import WatchManager, Notifier, ProcessEvent, IN_CREATE, IN_ISDIR

# Script Generator
import configuration

# Constants
header_fields = {
    "src_port": { # TCP Header
        "protocol": "tcp",
        "field": "src_port",
        "size": 16,
        "length": 16,
        "offset": 0
    },
    "dst_port": {
        "protocol": "tcp",
        "field": "dst_port",
        "size": 16,
        "length": 16,
        "offset": 0
    },
    "seq_num": {
        "protocol": "tcp",
        "field": "seq_num",
        "size": 32,
        "length": 32,
        "offset": 0
    },
    "ack_num": {
        "protocol": "tcp",
        "field": "ack_num",
        "size": 32,
        "length": 32,
        "offset": 0
    },
    "data_off": {
        "protocol": "tcp",
        "field": "data_off",
        "size": 8,
        "length": 4,
        "offset": 4
    },
    "tcp_reserved": {
        "protocol": "tcp",
        "field": "reserved",
        "size": 8,
        "length": 4,
        "offset": 4
    },
    "crw_flag": {
        "protocol": "tcp",
        "field": "flags",
        "size": 8,
        "length": 1,
        "offset": 0
    },
    "ece_flag": {
        "protocol": "tcp",
        "field": "flags",
        "size": 8,
        "length": 1,
        "offset": 1
    },
    "urg_flag": {
        "protocol": "tcp",
        "field": "flags",
        "size": 8,
        "length": 1,
        "offset": 2
    },
    "ack_flag": {
        "protocol": "tcp",
        "field": "flags",
        "size": 8,
        "length": 1,
        "offset": 3
    },
    "psh_flag": {
        "protocol": "tcp",
        "field": "flags",
        "size": 8,
        "length": 1,
        "offset": 4
    },
    "rst_flag": {
        "protocol": "tcp",
        "field": "flags",
        "size": 8,
        "length": 1,
        "offset": 5,
    },
    "syn_flag": {
        "protocol": "tcp",
        "field": "flags",
        "size": 8,
        "length": 1,
        "offset": 6
    },
    "fin_flag": {
        "protocol": "tcp",
        "field": "flags",
        "size": 8,
        "length": 1,
        "offset": 7
    },
    "win_size": {
        "protocol": "tcp",
        "field": "win_size",
        "size": 16,
        "length": 16,
        "offset": 0
    },
    "tcp_checksum": {
        "protocol": "tcp",
        "field": "checksum",
        "size": 16,
        "length": 16,
        "offset": 0
    },
    "urg_pointer": {
        "protocol": "tcp",
        "field": "urg_pointer",
        "size": 16,
        "length": 16,
        "offset": 0
    },
    "ip_version": {
        "protocol": "ip",
        "field": "version_ihl",
        "size": 8,
        "length": 4,
        "offset": 0
    },
    "ihl": {
        "protocol": "ip",
        "field": "version_ihl",
        "size": 8,
        "length": 4,
        "offset": 4
    },
    "dscp": {
        "protocol": "ip",
        "field": "dscp_esn",
        "size": 8,
        "length": 6,
        "offset": 0
    },
    "ecn": {
        "protocol": "ip",
        "field": "dscp_esn",
        "size": 8,
        "length": 2,
        "offset": 6
    },
    "tot_len": {
        "protocol": "ip",
        "field": "tot_len",
        "size": 16,
        "length": 16,
        "offset": 0
    },
    "iden": {
        "protocol": "ip",
        "field": "iden",
        "size": 16,
        "length": 16,
        "offset": 0
    },
    "reserved_flag": {
        "protocol": "ip",
        "field": "flags_fragoff",
        "size": 16,
        "length": 1,
        "offset": 0
    },
    "df_flag": {
        "protocol": "ip",
        "field": "flags_fragoff",
        "size": 16,
        "length": 1,
        "offset": 1
    },
    "mf_flag": {
        "protocol": "ip",
        "field": "flags_fragoff",
        "size": 16,
        "length": 1,
        "offset": 2
    },
    "fragment_offset": {
        "protocol": "ip",
        "field": "flags_fragoff",
        "size": 16,
        "length": 1,
        "offset": 3
    },
    "time_to_live": { 
        "protocol": "ip",
        "field": "TTL",
        "size": 16,
        "length": 8,
        "offset": 0
    },
    "protocol": {
        "protocol": "ip",
        "field": "protocol",
        "size": 16,
        "length": 8,
        "offset": 8
    },
    "ip_checksum": {
        "protocol": "ip",
        "field": "ip_checksum",
        "size": 16,
        "length": 16,
        "offset": 0
    },
    "src_addr": {
        "protocol": "ip",
        "field": "ip_checksum",
        "size": 32,
        "length": 32,
        "offset": 0
    },
    "dst_addr": {
        "protocol": "ip",
        "field": "dest_ip",
        "size": 32,
        "length": 32,
        "offset": 0
    },
    "version_ipv6": { # IPv6 Headers
        "protocol": "ip",
        "field": "dest_ip",
        "size": 4,
        "length": 4,
        "offset": 0
    },
    "traffic_class": {
        "protocol": "ip",
        "field": "dest_ip",
        "size": 6,
        "length": 6,
        "offset": 0
    },
    "flow_label": {
        "protocol": "ip",
        "field": "dest_ip",
        "size": 20,
        "length": 20,
        "offset": 0
    },
    "payload_length": {
        "protocol": "ip",
        "field": "dest_ip",
        "size": 16,
        "length": 16,
        "offset": 0
    },
    "next_header": {
        "protocol": "ip",
        "field": "dest_ip",
        "size": 8,
        "length": 8,
        "offset": 0
    },
    "hop_limit": {
        "protocol": "ip",
        "field": "dest_ip",
        "size": 8,
        "length": 8,
        "offset": 0
    },
    "source_address_IPv6": {
        "protocol": "ip",
        "field": "dest_ip",
        "size": 128,
        "length": 128,
        "offset": 0
    },
    "destination_address_IPv6": {
        "protocol": "ip",
        "field": "dest_ip",
        "size": 128,
        "length": 128,
        "offset": 0
    }
}

# Variables
notifier: Notifier = None
script_list = {}
scripts_written = False
debug = True


def generate_scripts(test_cases, templates_filenames):
    """
    Generate scripts from test cases and templates
    """
    global script_list
    global scripts_written
    remove_scripts()
    setup_watch_manager(configuration.generated_folder)
    templates = preload_templates(templates_filenames)
    for test_case in test_cases:
        single_cases = create_individual_cases(test_case)
        for index, case in enumerate(single_cases):
            script_list = generate_case(case, test_case["name"], templates, index)
            logging.info("Script_list has been generated")
            scripts_written = False
            while not scripts_written:
                try:
                    logging.info("Is this printed 1")
                    if notifier.check_events(timeout=10000):
                        logging.info("Is this printed 2")
                        notifier.read_events()
                        notifier.process_events()
                except KeyboardInterrupt:
                    notifier.stop()
                    exit()
                

def remove_scripts():
    """
    Function to remove generated_folder only if it exists
    """
    shutil.rmtree(configuration.generated_folder)
    os.mkdir(configuration.generated_folder)


def create_individual_cases(test_case):
    """
    Generates test data to represent every script from a single test case
    """
    result = [[]]
    for mutation in test_case["mutations"]:
        if isinstance(mutation["values"], str) and mutation["values"] == "all":
            mutation["values"] = []
            for i in range(pow(2, header_fields[mutation["field"]]["length"])):
                mutation["values"].append(i)
        result_copy = copy.deepcopy(result)
        for i in range(len(mutation["values"]) - 1):
            result = result + copy.deepcopy(result_copy)
        for index, value in enumerate(mutation["values"]):
            test = {}
            test["name"] = test_case["name"]
            test["operation"] = test_case["operation"]
            test["header"] = test_case["protocol"]
            if (test_case["operation"] == "rep"):
                test["field"] = header_fields[mutation["field"]]["field"]
                test["value"] = format_value(value, header_fields[mutation["field"]]["size"], header_fields[mutation["field"]]["length"], header_fields[mutation["field"]]["offset"])
            elif (test_case["operation"] == "ins"):
                test["field"] = test_case["offset"]
                test["value"] = value
            elif (test_case["operation"] == "trun"):
                test["field"] = value
                test["value"] = 0
            for i in range(len(result)):
                if (i * len(mutation["values"])) // len(result) == index:
                    flag = False
                    if test_case["operation"] == "rep":
                        for r in result[i]:
                            if r["field"] == header_fields[mutation["field"]]["field"]:
                                r["value"] = format_value(int(r["value"], 16) | int(test["value"], 16), header_fields[mutation["field"]]["size"], header_fields[mutation["field"]]["size"], 0)
                                flag = True
                                break
                    if not flag:
                        result[i].append(test)
    return result
    

def format_value(value, size, length, offset):
    """ 
    Format a value in the corresponding hexadecimal 
    """
    if size % 8 == 0:
        return ("0x{:0" + str(size // 4) + "X}").format(value * pow(2, size - (length + offset)))
    else:
        return ("0x{:0" + str(size + (size - (size % 8)) // 4) + "X}").format(value * pow(2, size - (length + offset)))


def generate_case(test_case, name, templates, index):
    """
    Write the script to a file
    """
    script_list = {}
    for i, template in enumerate(templates):
        expression = generate_expresion(test_case)
        content = template.format(expression)
        script_filename = "packetdrill_script_{0}_{1}_{2}.pkt".format(name, i, index)
        script_list[script_filename] = content
        # with open(script_filename, "w") as script_file:
        #     script_file.write(content)
    return script_list
        

def generate_expresion(test_case): #TODO: Hardcoded header
    """
    Generate the mut expression to add into the template
    """
    return "{{{0}}}".format(" ; ".join(["{0} {1} {2} {3}".format(x["opcode"], x["header"], x["field"], x["value"]) for x in test_case]))
    

def preload_templates(filenames):
    """
    Load the content of the templates
    """
    templates = []
    for template in filenames:
        with open(template, "r") as template_file:
            templates.append(template_file.read())
    return templates


def setup_watch_manager(watch_dir):
    """
    Setup the watch manager to trigger event when 
    a file is created
    """
    global notifier
    wm = WatchManager()
    mask = IN_CREATE 
    wm.add_watch(watch_dir, mask, auto_add=True)
    notifier = Notifier(wm, EventHandler())


class EventHandler(ProcessEvent):
    """
    Event handler for file creation
    """
    def process_IN_CREATE(self, event):
        """
        Function to trigger in create script file
        """
        global scripts_written
        logging.info(f"Event called for pathname: {event.pathname}")

        if not event.mask & IN_ISDIR and os.path.basename(event.pathname) == "index.txt":
            # This method is called when a new file is created in the directory
            # if event.name == 'myfile.txt':
            #     print("My file was created: %s" % os.path.join(event.path, event.name))

            # We copy because script_list can get updated any time
            script_list_copy = copy.deepcopy(script_list)

            for script_name in script_list_copy:
                script_content = script_list_copy[script_name]
                script_path = os.path.join(event.path, script_name)

                with open(script_path, "w") as script_file:
                    script_file.write(script_content)

            with open(event.pathname, 'w') as event_file:
                event_file.write("Completed")

            scripts_written = True
