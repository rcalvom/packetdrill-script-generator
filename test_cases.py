""" List with Test Cases to generate and excecute """

test_cases = [
    # {
    #     "name": "source_port",
    #     "mutations" : [
    #         {
    #             "field": "src_port",
    #             "values": [
    #                 0x0000,
    #                 0xFFFF
    #             ]
    #         }
    #     ]
    # },
    # {
    #     "name": "destination_port",
    #     "mutations" : [
    #         {
    #             "field": "dst_port",
    #             "values": [
    #                 0x0000,
    #                 0xFFFF
    #             ]
    #         }
    #     ]
    # },
    # {
    #     "name": "sequence_number",
    #     "mutations" : [
    #         {
    #             "field": "seq_num",
    #             "values": [
    #                 0x00000000,
    #                 0xFFFFFFFF
    #             ]
    #         },
    #         {
    #             "field": "syn_flag",
    #             "values": [
    #                 0,
    #                 1
    #             ]
    #         }
    #     ]
    # },
    # {
    #     "name": "acknowledgment_number",
    #     "mutations" : [
    #         {
    #             "field": "ack_num",
    #             "values": [
    #                 0x00000000,
    #                 0xFFFFFFFF
    #             ]
    #         },
    #         {
    #             "field": "ack_flag",
    #             "values": [
    #                 0,
    #                 1
    #             ]
    #         }
    #     ]
    # },
    {
        "name": "data_offset",
        "opcode": "rep",
        "protocol": "tcp",
        "mutations" : [
            {
                "field": "data_off",
                "values": [
                    0x0,
                    0x5,
                    0xA,
                    0xF
                ]
            },
            {
                "field": "tcp_reserved",
                "values": [
                    0x0,
                    0x5,
                    0xA,
                    0xF
                ]
            }
        ]
    },
    # {
    #     "name": "tcp_reserved",
    #     "mutations" : [
    #         {
    #             "field": "tcp_reserved",
    #             "values": "all"
    #         }
    #     ]
    # },
    # {
    #     "name": "tcp_flags",
    #     "mutations" : [
    #         {
    #             "field": "crw_flag",
    #             "values": [
    #                 0,
    #                 1
    #             ]
    #         },
    #         {
    #             "field": "ece_flag",
    #             "values": [
    #                 0,
    #                 1
    #             ]
    #         },
    #         {
    #             "field": "urg_flag",
    #             "values": [
    #                 0,
    #                 1
    #             ]
    #         },
    #         {
    #             "field": "ack_flag",
    #             "values": [
    #                 0,
    #                 1
    #             ]
    #         },
    #         {
    #             "field": "psh_flag",
    #             "values": [
    #                 0,
    #                 1
    #             ]
    #         },
    #         {
    #             "field": "rst_flag",
    #             "values": [
    #                 0,
    #                 1
    #             ]
    #         },
    #         {
    #             "field": "syn_flag",
    #             "values": [
    #                 0,
    #                 1
    #             ]
    #         },
    #         {
    #             "field": "fin_flag",
    #             "values": [
    #                 0,
    #                 1
    #             ]
    #         }
    #     ]
    # },
    # {
    #     "name": "windows_size",
    #     "mutations" : [
    #         {
    #             "field": "win_size",
    #             "values": [
    #                 0x0000,
    #                 0xFFFF
    #             ]
    #         }
    #     ]
    # },
    # {
    #     "name": "checksum",
    #     "mutations" : [
    #         {
    #             "field": "tcp_checksum",
    #             "values": [
    #                 0x0000,
    #                 0xFFFF
    #             ]
    #         }
    #     ]
    # },
    # {
    #     "name": "urg_pointer",
    #     "mutations" : [
    #         {
    #             "field": "urg_pointer",
    #             "values": [
    #                 0x0000,
    #                 0xFFFF
    #             ]
    #         },
    #         {
    #             "field": "urg_flag",
    #             "values": [
    #                 0,
    #                 1
    #             ]
    #         }
    #     ]
    # },
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
        #     "name": "version_ihl",
        #     "opcode": "rep",
        #     "protocol": "ipv4",
        #     "mutations" : [
        #         {
        #             "field": "ip_version",
        #             "values": [
        #                 0x0,
        #                 0x4,
        #                 0x6,
        #                 0xF
        #             ]
        #         },
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

        # {
        #     "name": "mss_option",
        #     "opcode": "ins",
        #     "protocol": "tcp",
        #     "offset": "20",
        #     "mutations" : [
        #         {
        #             "values": [
        #                 "0x02040000",
        #                 "0x02041111",
        #                 "0x02045555",
        #                 "0x0204AAAA",
        #                 "0x0204FFFF",
        #                 "0x02030000",
        #                 "0x02031111",
        #                 "0x02035555",
        #                 "0x0203AAAA",
        #                 "0x0203FFFF",
        #                 "0x02050000",
        #                 "0x02051111",
        #                 "0x02055555",
        #                 "0x0205AAAA",
        #                 "0x0205FFFF",
        #             ]
        #         }
        #     ]
        # },

        # {
        #     "name": "wscale_option",
        #     "opcode": "ins",
        #     "protocol": "tcp",
        #     "offset": "20",
        #     "mutations" : [
        #         {
        #             "values": [
        #                 "0x030400",
        #                 "0x03041111",
        #                 "0x030455",
        #                 "0x0304AAAA",
        #                 "0x0304FF",
        #                 "0x03030000",
        #                 "0x030311",
        #                 "0x03035555",
        #                 "0x0303AA",
        #                 "0x0303FFFF",
        #                 "0x030200",
        #                 "0x03021111",
        #                 "0x030255",
        #                 "0x0302AAAA",
        #                 "0x0302FF",
        #             ]
        #         }
        #     ]
        # },
        # {
        #     "name": "ip_option",
        #     "opcode": "ins",
        #     "protocol": "ipv4",
        #     "offset": "20",
        #     "mutations" : [
        #         {
        #             "values": [
        #                 "0x030400",
        #                 "0x03041111",
        #                 "0x030455030400",
        #                 "0x0304AAAA030400030400",
        #                 "0x0304FF030400030400030400",
        #                 "0x03040000",
        #                 "0x030411030400",
        #                 "0x03035555030400030400030400030400",
        #                 "0x0303AA030400030400030400030400030400"
        #             ]
        #         }
        #     ]
        # },
        # {
        #     "name": "trun_tcp",
        #     "opcode": "trun",
        #     "protocol": "tcp",
        #     "mutations": [
        #         {
        #             "values": [
        #                 "0", "1", "5", "10", "15", "20"
        #             ]
        #         }
        #     ]
        # },
]

