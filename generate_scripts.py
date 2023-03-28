""" Functions to generate Packetdrill scripts based on test cases list """

# System
import logging
import shutil
import copy
import os

# Notify
import pyinotify

# Script Generator
import configuration

# Constants
header_fields = {
    "src_port": {
        "protocol": "tcp",
        "field": "src_port",
        "size": 16
    },
    "dst_port": {
        "protocol": "tcp",
        "field": "dst_port",
        "size": 16
    },
    "seq_num": {
        "protocol": "tcp",
        "field": "seq_num",
        "size": 32
    },
    "ack_num": {
        "protocol": "tcp",
        "field": "ack_num",
        "size": 32
    },
    "data_off": {
        "protocol": "tcp",
        "field": "data_off",
        "size": 4
    },
    "reserved": {
        "protocol": "tcp",
        "field": "reserved",
        "size": 4
    },
    "crw_flag": {
        "protocol": "tcp",
        "field": "crw_flag",
        "size": 1,
    },
    "ece_flag": {
        "protocol": "tcp",
        "field": "ece_flag",
        "size": 1,
    },
    "urg_flag": {
        "protocol": "tcp",
        "field": "urg_flag",
        "size": 1,
    },
    "ack_flag": {
        "protocol": "tcp",
        "field": "ack_flag",
        "size": 1,
    },
    "psh_flag": {
        "protocol": "tcp",
        "field": "psh_flag",
        "size": 1,
    },
    "rst_flag": {
        "protocol": "tcp",
        "field": "rst_flag",
        "size": 1,
    },
    "syn_flag": {
        "protocol": "tcp",
        "field": "syn_flag",
        "size": 1,
    },
    "fin_flag": {
        "protocol": "tcp",
        "field": "fin_flag",
        "size": 1,
    },
    "win_size": {
        "protocol": "tcp",
        "field": "win_size",
        "size": 16
    },
    "tcp_checksum": {
        "protocol": "tcp",
        "field": "checksum",
        "size": 16
    },
    "urg_pointer": {
        "protocol": "tcp",
        "field": "urg_pointer",
        "size": 16
    },
    "ipv4_version": {
        "protocol": "ipv4",
        "field": "version",
        "size": 4,
    },
    "ihl": {
        "protocol": "ipv4",
        "field": "ihl",
        "size": 4,
    },
    "dscp": {
        "protocol": "ipv4",
        "field": "dscp",
        "size": 6,
    },
    "ecn": {
        "protocol": "ipv4",
        "field": "ecn",
        "size": 2
    },
    "tot_len": {
        "protocol": "ipv4",
        "field": "tot_len",
        "size": 16
    },
    "iden": {
        "protocol": "ipv4",
        "field": "iden",
        "size": 16
    },
    "rsv_flag": {
        "protocol": "ipv4",
        "field": "rsv_flag",
        "size": 1
    },
    "df_flag": {
        "protocol": "ipv4",
        "field": "df_flag",
        "size": 1
    },
    "mf_flag": {
        "protocol": "ipv4",
        "field": "mf_flag",
        "size": 1
    },
    "fragment_offset": {
        "protocol": "ipv4",
        "field": "frag_off",
        "size": 13
    },
    "time_to_live": { 
        "protocol": "ipv4",
        "field": "ttl",
        "size": 8
    },
    "protocol": {
        "protocol": "ipv4",
        "field": "protocol",
        "size": 8
    },
    "ip_checksum": {
        "protocol": "ipv4",
        "field": "checksum",
        "size": 16
    },
    "src_addr": {
        "protocol": "ipv4",
        "field": "src_addr",
        "size": 32
    },
    "dst_addr": {
        "protocol": "ipv4",
        "field": "dst_addr",
        "size": 32
    },
    "ipv6_version": {
        "protocol": "ipv6",
        "field": "version",
        "size": 4
    },
    "traffic_class": {
        "protocol": "ipv6",
        "field": "trf_class",
        "size": 8
    },
    "flow_label": {
        "protocol": "ipv6",
        "field": "flow_label",
        "size": 20
    },
    "payload_length": {
        "protocol": "ipv6",
        "field": "pyld_len",
        "size": 16
    },
    "next_header": {
        "protocol": "ipv6",
        "field": "next_header",
        "size": 8
    },
    "hop_limit": {
        "protocol": "ipv6",
        "field": "hop_limit",
        "size": 8
    },
    "src_addr_ipv6": {
        "protocol": "ipv6",
        "field": "src_addr",
        "size": 128
    },
    "dst_addr_ipv6": {
        "protocol": "ipv6",
        "field": "dst_addr",
        "size": 128
    }
}

operations = {
    "replacement": "rep",
    "truncate": "trun",
    "insert": "ins"
}

# Variables
notifier = None
script_list = {}
scripts_written = False


def generate_scripts(test_cases, templates_filenames):
    """
    Generate scripts from test cases and templates
    """
    global script_list, scripts_written
    remove_scripts()
    setup_watch_manager(configuration.generated_folder)
    templates = preload_templates(templates_filenames)
    for test_case in test_cases:
        single_cases = create_individual_cases(test_case)
        for index, case in enumerate(single_cases):
            script_list = generate_case(case, test_case["name"], templates, index)
            logging.debug("Script_list has been generated")
            scripts_written = False
            while not scripts_written:
                try:
                    if notifier.check_events(timeout=10000):
                        notifier.read_events()
                        notifier.process_events()
                except KeyboardInterrupt:
                    notifier.stop()
                    exit()
    script_list = {}
    scripts_written = False
    while not scripts_written:
        try:
            if notifier.check_events(timeout=10000):
                notifier.read_events()
                notifier.process_events()
        except KeyboardInterrupt:
            notifier.stop()
            exit()
                


def remove_scripts():
    """
    Remove scripts if exist
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
            for i in range(pow(2, header_fields[mutation["field"]]["size"])):
                mutation["values"].append(i)
        result_copy = copy.deepcopy(result)
        for i in range(len(mutation["values"]) - 1):
            result = result + copy.deepcopy(result_copy)
        for index, value in enumerate(mutation["values"]):
            test = {}
            test["name"] = test_case["name"]
            test["header"] = header_fields[mutation["field"]]["protocol"]
            test["field"] = header_fields[mutation["field"]]["field"]
            test["value"] = format_value(value, header_fields[mutation["field"]]["size"])
            test["operation"] = mutation["operation"]
            for i in range(len(result)):
                if (i * len(mutation["values"])) // len(result) == index:
                    result[i].append(test)
    return result
    

def format_value(value, size):
    """ 
    Format a value in the corresponding hexadecimal 
    """
    if size % 8 == 0:
        return ("0x{:0" + str(size // 4) + "X}").format(value)
    else:
        return ("0x{:0" + str((size + (8 - (size % 8))) // 4) + "X}").format(value)


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
        #    script_file.write(content)
    return script_list
        

def generate_expresion(test_case): #TODO: Hardcoded header
    """
    Generate the expression to add into the template
    """
    return "{{{0}}}".format(" ; ".join(["{0} {1} {2} {3}".format(operations[x["operation"]], x["header"], x["field"], x["value"]) for x in test_case]))
    

def preload_templates(filenames):
    """
    Load the content of the templates
    """
    templates = []
    for template in filenames:
        with open(template, "r") as template_file:
            templates.append(template_file.read())
    return templates


def setup_watch_manager(watch_directory):
    """
    Set up the watch manager and notifier
    """
    global notifier
    wm = pyinotify.WatchManager()
    mask = pyinotify.IN_CREATE 
    wm.add_watch(watch_directory, mask, auto_add=True)
    notifier = pyinotify.Notifier(wm, EventHandler())
        

class EventHandler(pyinotify.ProcessEvent):
    """
    Class to define the event handler
    """
    def process_IN_CREATE(self, event):
        """
        This method is called when a new file is created in the directory
        """
        global scripts_written
        logging.debug("Event called for pathname: {0}".format(event.pathname))
        if not event.mask & pyinotify.IN_ISDIR and os.path.basename(event.pathname) == "index.txt":
            # if event.name == 'myfile.txt':
            #     print("My file was created: %s" % os.path.join(event.path, event.name))
            if (len(script_list) == 0):
                with open(event.pathname, 'w') as event_file:
                    event_file.write("Finished")
            else:
                # We copy because script_list can get updated any time
                script_list_copy = copy.deepcopy(script_list)
                for script_name in script_list_copy:
                    print(event.path)
                    script_content = script_list_copy[script_name]
                    script_path = os.path.join(event.path, script_name)
                    with open(script_path, "w") as script_file:
                        script_file.write(script_content)
                # We tell the consumer that we are done writing 
                with open(event.pathname, 'w') as event_file:
                    event_file.write("Completed")
            scripts_written = True