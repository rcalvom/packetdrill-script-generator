""" List with Test Cases to generate and excecute """

test_cases = [
    {
        "name": "source_port",
        "mutations" : [
            {
                "field": "src_port",
                "operation": "replacement",
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
                "operation": "replacement",
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
                "operation": "replacement",
                "values": [
                    0x00000000,
                    0xFFFFFFFF
                ]
            },
            {
                "field": "syn_flag",
                "operation": "replacement",
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
                "operation": "replacement",
                "values": [
                    0x00000000,
                    0xFFFFFFFF
                ]
            },
            {
                "field": "ack_flag",
                "operation": "replacement",
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
                "operation": "replacement",
                "values": [
                    0x0,
                    0xF
                ]
            }
        ]
    },
    {
        "name": "reserved",
        "mutations" : [
            {
                "field": "reserved",
                "operation": "replacement",
                "values": "all"
            }
        ]
    },
    # {
    #     "name": "tcp_flags",
    #     "mutations" : [
    #         {
    #             "field": "cwr_flag",
    #             "operation": "replacement",
    #             "values": "all"
    #         },
    #         {
    #             "field": "ece_flag",
    #             "operation": "replacement",
    #             "values": "all"
    #         },
    #         {
    #             "field": "urg_flag",
    #             "operation": "replacement",
    #             "values": "all"
    #         },
    #         {
    #             "field": "ack_flag",
    #             "operation": "replacement",
    #             "values": "all"
    #         },
    #         {
    #             "field": "psh_flag",
    #             "operation": "replacement",
    #             "values": "all"
    #         },
    #         {
    #             "field": "rst_flag",
    #             "operation": "replacement",
    #             "values": "all"
    #         },
    #         {
    #             "field": "syn_flag",
    #             "operation": "replacement",
    #             "values": "all"
    #         },
    #         {
    #             "field": "fin_flag",
    #             "operation": "replacement",
    #             "values": "all"
    #         }
    #     ]
    # },
    {
        "name": "windows_size",
        "mutations" : [
            {
                "field": "win_size",
                "operation": "replacement",
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
                "operation": "replacement",
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
                "operation": "replacement",
                "values": [
                    0x0000,
                    0xFFFF
                ]
            },
            {
                "field": "urg_flag",
                "operation": "replacement",
                "values": [
                    0,
                    1
                ]
            }
        ]
    },
    {
        "name": "mss_option",
        "mutations" : [
            {
                "field": "mss_option",
                "operation": "insert",
                "values": [
                    "0x02040000",
                    "0x02041111",
                    "0x02045555",
                    "0x0204AAAA",
                    "0x0204FFFF",
                    "0x02030000",
                    "0x02031111",
                    "0x02035555",
                    "0x0203AAAA",
                    "0x0203FFFF",
                    "0x02050000",
                    "0x02051111",
                    "0x02055555",
                    "0x0205AAAA",
                    "0x0205FFFF",
                ]
            }
        ]
    },
    {
        "name": "wscale_option",
        "mutations" : [
            {
                "field": "wscale_option",
                "operation": "insert",
                "values": [
                    "0x030400",
                    "0x03041111",
                    "0x030455",
                    "0x0304AAAA",
                    "0x0304FF",
                    "0x03030000",
                    "0x030311",
                    "0x03035555",
                    "0x0303AA",
                    "0x0303FFFF",
                    "0x030200",
                    "0x03021111",
                    "0x030255",
                    "0x0302AAAA",
                    "0x0302FF"
                ]
            }
        ]
    },
    {
        "name": "trun_tcp",
        "mutations": [
            {
                "field": "trun_tcp",
                "operation": "truncate",
                "values": [
                    "0", 
                    "1", 
                    "5", 
                    "10", 
                    "15", 
                    "20"
                ]
            }
        ]
    }
]

