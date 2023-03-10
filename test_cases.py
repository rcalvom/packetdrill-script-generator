""" List with Test Cases to generate and excecute """

test_cases = [
    {
        "name": "source_port",
        "mutations" : [
            {
                "field": "src_port",
                "values": [
                    0x0000,
                    0xFFFF
                ]
            }
        ]
    },
    {
        "name": "destination_port",
        "mutations" : [
            {
                "field": "dst_port",
                "values": [
                    0x0000,
                    0xFFFF
                ]
            }
        ]
    },
    {
        "name": "sequence_number",
        "mutations" : [
            {
                "field": "seq_num",
                "values": [
                    0x00000000,
                    0xFFFFFFFF
                ]
            },
            {
                "field": "syn_flag",
                "values": [
                    0,
                    1
                ]
            }
        ]
    },
    {
        "name": "acknowledgment_number",
        "mutations" : [
            {
                "field": "ack_num",
                "values": [
                    0x00000000,
                    0xFFFFFFFF
                ]
            },
            {
                "field": "ack_flag",
                "values": [
                    0,
                    1
                ]
            }
        ]
    },
    {
        "name": "data_offset",
        "mutations" : [
            {
                "field": "data_off",
                "values": [
                    0x0,
                    0xF
                ]
            }
        ]
    },
    {
        "name": "tcp_reserved",
        "mutations" : [
            {
                "field": "tcp_reserved",
                "values": "all"
            }
        ]
    },
    {
        "name": "tcp_flags",
        "mutations" : [
            {
                "field": "crw_flag",
                "values": [
                    0,
                    1
                ]
            },
            {
                "field": "ece_flag",
                "values": [
                    0,
                    1
                ]
            },
            {
                "field": "urg_flag",
                "values": [
                    0,
                    1
                ]
            },
            {
                "field": "ack_flag",
                "values": [
                    0,
                    1
                ]
            },
            {
                "field": "psh_flag",
                "values": [
                    0,
                    1
                ]
            },
            {
                "field": "rst_flag",
                "values": [
                    0,
                    1
                ]
            },
            {
                "field": "syn_flag",
                "values": [
                    0,
                    1
                ]
            },
            {
                "field": "fin_flag",
                "values": [
                    0,
                    1
                ]
            }
        ]
    },
    {
        "name": "windows_size",
        "mutations" : [
            {
                "field": "win_size",
                "values": [
                    0x0000,
                    0xFFFF
                ]
            }
        ]
    },
    {
        "name": "checksum",
        "mutations" : [
            {
                "field": "tcp_checksum",
                "values": [
                    0x0000,
                    0xFFFF
                ]
            }
        ]
    },
    {
        "name": "urg_pointer",
        "mutations" : [
            {
                "field": "urg_pointer",
                "values": [
                    0x0000,
                    0xFFFF
                ]
            },
            {
                "field": "urg_flag",
                "values": [
                    0,
                    1
                ]
            }
        ]
    }
]

