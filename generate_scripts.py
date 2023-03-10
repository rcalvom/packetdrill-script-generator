""" Functions to generate Packetdrill scripts based on test cases list """

# System
import logging
import copy

# Constants
header_fields = {
    "src_port": {
        "protocol": "tcp",
        "field": "src_port",
        "size": 16,
        "offset": 0
    },
    "dst_port": {
        "protocol": "tcp",
        "field": "dst_port",
        "size": 16,
        "offset": 0
    },
    "seq_num": {
        "protocol": "tcp",
        "field": "seq_num",
        "size": 32,
        "offset": 0
    },
    "ack_num": {
        "protocol": "tcp",
        "field": "ack_num",
        "size": 32,
        "offset": 0
    },
    "data_off": {
        "protocol": "tcp",
        "field": "tcp_hdr_len",
        "size": 4,
        "offset": 0
    },
    "tcp_reserved": {
        "protocol": "tcp",
        "field": "tcp_hdr_len",
        "size": 4,
        "offset": 4
    },
    "crw_flag": {
        "protocol": "tcp",
        "field": "flags",
        "size": 1,
        "offset": 0
    },
    "ece_flag": {
        "protocol": "tcp",
        "field": "flags",
        "size": 1,
        "offset": 1
    },
    "urg_flag": {
        "protocol": "tcp",
        "field": "flags",
        "size": 1,
        "offset": 2
    },
    "ack_flag": {
        "protocol": "tcp",
        "field": "flags",
        "size": 1,
        "offset": 3
    },
    "psh_flag": {
        "protocol": "tcp",
        "field": "flags",
        "size": 1,
        "offset": 4
    },
    "rst_flag": {
        "protocol": "tcp",
        "field": "flags",
        "size": 1,
        "offset": 5
    },
    "syn_flag": {
        "protocol": "tcp",
        "field": "flags",
        "size": 1,
        "offset": 6
    },
    "fin_flag": {
        "protocol": "tcp",
        "field": "flags",
        "size": 1,
        "offset": 7
    },
    "win_size": {
        "protocol": "tcp",
        "field": "win_size",
        "size": 16,
        "offset": 0
    },
    "tcp_checksum": {
        "protocol": "tcp",
        "field": "tcp_checksum",
        "size": 16,
        "offset": 0
    },
    "urg_pointer": {
        "protocol": "tcp",
        "field": "urg_pointer",
        "size": 16,
        "offset": 0
    }
}

def generate_scripts(test_cases, templates_filenames):
    """
    Generate scripts from test cases and templates
    """
    templates = preload_templates(templates_filenames)
    for test_case in test_cases:
        single_cases = create_individual_cases(test_case)
        for index, case in enumerate(single_cases):
            generate_case(case, test_case["name"], templates, index)


def create_individual_cases(test_case):
    """
    Generates test data to represent every script from a single test case
    """
    result = [[]]
    for mutation in test_case["mutations"]: 
        result_copy = copy.deepcopy(result)
        for i in range(len(mutation["values"]) - 1):
            result = result + result_copy
        for index, value in enumerate(mutation["values"]):
            test = {}
            if mutation["field"] in ['crw_flag', 'ece_flag', 'urg_flag', 'ack_flag', 'psh_flag', 'rst_flag', 'syn_flag', 'fin_flag']:
                test["name"] = test_case["name"]
                test["header"] = "tcp"
                test["field"] = 'flags'               
            if mutation["field"] == 'crw_flag':
                test["value"] = format_value(value * 0x80, mutation["size"])
            elif mutation["field"] == 'ece_flag':
                test["value"] = format_value(value * 0x40, mutation["size"])
            elif mutation["field"] == 'urg_flag':
                test["value"] = format_value(value * 0x20, mutation["size"])
            elif mutation["field"] == 'ack_flag':
                test["value"] = format_value(value * 0x10, mutation["size"])
            elif mutation["field"] == 'psh_flag':
                test["value"] = format_value(value * 0x08, mutation["size"])
            elif mutation["field"] == 'rst_flag':
                test["value"] = format_value(value * 0x04, mutation["size"])
            elif mutation["field"] == 'syn_flag':
                test["value"] = format_value(value * 0x02, mutation["size"])
            elif mutation["field"] == 'fin_flag':
                test["value"] = format_value(value * 0x01, mutation["size"])
            elif mutation["field"] == 'data_off':
                test["value"] = format_value(value * 0x1000, mutation["size"])
            elif mutation["field"] == 'reserved':
                test["value"] = format_value(value * 0x0100, mutation["size"])
            else:
                test["name"] = test_case["name"]
                test["header"] = "tcp"
                test["field"] = mutation["field"]
                test["value"] = format_value(value, mutation["size"])
            for i in range(len(result)):
                if (i * len(mutation["values"])) // len(result) == index:
                    if test["field"] == 'flags':
                        flag = False
                        for r in result[i]:
                            if r["field"] == 'flags':
                                r["value"] = format_value(int(r["value"], 16) | int(test["value"], 16), 8)
                                flag = True
                                break
                        if flag == False:
                            result[i].append(test)
                    else:
                        result[i].append(test)
    return result
    

def format_value(value, size):
    """ 
    Format a value in the corresponding hexadecimal 
    """
    if size % 4 == 0:
        s = size
    elif size % 4 == 1:
        s = size + 3
    elif size % 4 == 2:
        s = size + 2
    elif size % 4 == 3:
        s = size + 1
    if (s // 4) % 2 == 1:
        s = s + 4
    return ("0x{:0" + str(s//4) + "x}").format(value)

def generate_case(test_case, name, templates, index):
    """
    Write the script to a file
    """
    for i, template in enumerate(templates):
        expression = generate_expresion(test_case)
        content = template.format(expression)
        script_filename = "scripts/packetdrill_script_{0}_{1}_{2}.pkt".format(name, i, index)
        with open(script_filename, "w") as script_file:
            script_file.write(content)
        

def generate_expresion(test_case): #TODO: Hardcoded header
    """
    Generate the mut expression to add into the template
    """
    return "{{{0}}}".format(" ; ".join(["{0} {1} {2} {3}".format("rep", x["header"], x["field"], x["value"]) for x in test_case]))
    

def preload_templates(filenames):
    """
    Load the content of the templates
    """
    templates = []
    for template in filenames:
        with open(template, "r") as template_file:
            templates.append(template_file.read())
    return templates
        