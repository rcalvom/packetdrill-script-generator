""" List with Test Cases for TCP Protocol """

test_cases = [
    {
        "name": "source_port",
        "mutations" : [
            {
                "field": "src_port",
                "operation": "replace",
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
                "operation": "replace",
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
                "operation": "replace",
                "values": [
                    0x00000000,
                    0xFFFFFFFF
                ]
            },
            {
                "field": "syn_flag",
                "operation": "replace",
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
                "operation": "replace",
                "values": [
                    0x00000000,
                    0xFFFFFFFF
                ]
            },
            {
                "field": "ack_flag",
                "operation": "replace",
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
                "operation": "replace",
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
                "operation": "replace",
                "values": "all"
            }
        ]
    },
    # {
    #     "name": "tcp_flags",
    #     "mutations" : [
    #         {
    #             "field": "cwr_flag",
    #             "operation": "replace",
    #             "values": "all"
    #         },
    #         {
    #             "field": "ece_flag",
    #             "operation": "replace",
    #             "values": "all"
    #         },
    #         {
    #             "field": "urg_flag",
    #             "operation": "replace",
    #             "values": "all"
    #         },
    #         {
    #             "field": "ack_flag",
    #             "operation": "replace",
    #             "values": "all"
    #         },
    #         {
    #             "field": "psh_flag",
    #             "operation": "replace",
    #             "values": "all"
    #         },
    #         {
    #             "field": "rst_flag",
    #             "operation": "replace",
    #             "values": "all"
    #         },
    #         {
    #             "field": "syn_flag",
    #             "operation": "replace",
    #             "values": "all"
    #         },
    #         {
    #             "field": "fin_flag",
    #             "operation": "replace",
    #             "values": "all"
    #         }
    #     ]
    # },
    {
        "name": "windows_size",
        "mutations" : [
            {
                "field": "win_size",
                "operation": "replace",
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
                "operation": "replace",
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
                "operation": "replace",
                "values": [
                    0x0000,
                    0xFFFF
                ]
            },
            {
                "field": "urg_flag",
                "operation": "replace",
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

