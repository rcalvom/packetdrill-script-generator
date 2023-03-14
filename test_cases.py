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
    },
    # {
    #     "name": "ip_version",
    #     "mutations" : [
    #         {
    #             "field": "ip_version",
    #             "values": [
    #                 0x0,
    #                 0x4,
    #                 0x6,
    #                 0xF
    #             ]
    #         }
    #     ]
    # },
    # {
    #     "name": "internet_header_length",
    #     "mutations" : [
    #         {
    #             "field": "ihl",
    #             "values": [
    #                 0x0,
    #                 0x8,
    #                 0xF
    #             ]
    #         }
    #     ]
    # },
    # {
    #     "name": "differentiated_services_code_point",
    #     "mutations" : [
    #         {
    #             "field": "dscp",
    #             "values": [
    #                 0x00,
    #                 0xFC,
    #             ]
    #         }
    #     ]
    # },
    # {
    #     "name": "explicit_congestion_notification",
    #     "mutations" : [
    #         {
    #             "field": "ecn",
    #             "values": "all"
    #         }
    #     ]
    # },
    # {
    #     "name": "total_length",
    #     "mutations" : [
    #         {
    #             "field": "tot_len",
    #             "values": [
    #                 0x0000,
    #                 0x003F,
    #                 0x009F,
    #                 0xFFFF
    #             ]
    #         }
    #     ]
    # },
    # {
    #     "name": "identification",
    #     "mutations" : [
    #         {
    #             "field": "iden",
    #             "values": [
    #                 0x0000,
    #                 0xFFFF
    #             ]
    #         }
    #     ]
    # },
    # {
    #     "name": "ip_flags",
    #     "mutations" : [
    #         {
    #             "field": "reserved_flag",
    #             "values": [
    #                 0,
    #                 1
    #             ]
    #         },
    #         {
    #             "field": "df_flag",
    #             "values": [
    #                 0,
    #                 1
    #             ]
    #         },
    #         {
    #             "field": "mf_flag",
    #             "values": [
    #                 0,
    #                 1
    #             ]
    #         }
    #     ]
    # },
    # {
    #     "name": "fragment_offset",
    #     "mutations" : [
    #         {
    #             "field": "fragment_offset",
    #             "values": [
    #                 0x0000,
    #                 0x00F0,
    #                 0x1FFF
    #             ]
    #         }
    #     ]
    # },
    # {
    #     "name": "time_to_live",
    #     "mutations" : [
    #         {
    #             "field": "time_to_live",
    #             "values": [
    #                 0x00,
    #                 0xFF
    #             ]
    #         }
    #     ]
    # },
    # {
    #     "name": "protocol",
    #     "mutations" : [
    #         {
    #             "field": "protocol",
    #             "values": [
    #                 0x00,
    #                 0x06,
    #                 0x11,
    #                 0xFF
    #             ]
    #         }
    #     ]
    # },
    # {
    #     "name": "ip_checksum",
    #     "mutations" : [
    #         {
    #             "field": "ip_checksum",
    #             "values": [
    #                 0x0000,
    #                 0xFFFF
    #             ]
    #         }
    #     ]
    # },
    # {
    #     "name": "source_address",
    #     "mutations" : [
    #         {
    #             "field": "src_ip",
    #             "values": [
    #                 0x00000000,
    #                 0xFFFFFFFF,
    #                 0x7D004B00,
    #                 0x7D004BFF,
    #                 0x7D004B30,
    #                 0x78004B30,
    #                 0x78004B00,
    #                 0x78004BFF
    #             ]
    #         }
    #     ]
    # },
    #     {
    #     "name": "destiantion_address",
    #     "mutations" : [
    #         {
    #             "field": "dest_ip",
    #             "values": [
    #                 0x00000000,
    #                 0xFFFFFFFF,
    #                 0x7D004B00,
    #                 0x7D004BFF,
    #                 0x7D004B30,
    #                 0x78004B30,
    #                 0x78004B00,
    #                 0x78004BFF
    #             ]
    #         }
    #     ]
    # }, #TODO: CAMPOS OPCIONALES DE TCP y IP
]

