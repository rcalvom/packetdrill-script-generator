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
    }
]

