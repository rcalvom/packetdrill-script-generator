""" List with Test Cases to generate and excecute """
# 2352

test_cases = [
    # {
    #     "name": "source_port",
    #     "mutations" : [
    #         {
    #             "field": "src_port",
    #             "size": 16,
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
    #             "size": 16,
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
    #             "size": 32,
    #             "values": [
    #                 0x00000000,
    #                 0xFFFFFFFF
    #             ]
    #         },
    #         {
    #             "field": "syn_flag",
    #             "size": 1,
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
    #             "field": "seq_num",
    #             "size": 32,
    #             "values": [
    #                 0x00000000,
    #                 0xFFFFFFFF
    #             ]
    #         },
    #         {
    #             "field": "ack_flag",
    #             "size": 1,
    #             "values": [
    #                 0,
    #                 1
    #             ]
    #         }
    #     ]
    # },
    # {
    #     "name": "data_offset",
    #     "mutations" : [
    #         {
    #             "field": "data_off",
    #             "size": 4,
    #             "values": [
    #                 0x0,
    #                 0xF
    #             ]
    #         }
    #     ]
    # },
    # {
    #     "name": "reserved",
    #     "mutations" : [
    #         {
    #             "field": "reserved",
    #             "size": 4,
    #             "values": [
    #                 0x0,
    #                 0x1,
    #                 0x2,
    #                 0x3,
    #                 0x4,
    #                 0x5,
    #                 0x6,
    #                 0x7,
    #                 0x8,
    #                 0x9,
    #                 0xA,
    #                 0xB,
    #                 0xC,
    #                 0xD,
    #                 0xE,
    #                 0xF
    #             ]
    #         }
    #     ]
    # },
    {
        "name": "flags",
        "mutations" : [
            {
                "field": "crw_flag",
                "size": 1,
                "values": [
                    0,
                    1
                ]
            },
            {
                "field": "ece_flag",
                "size": 1,
                "values": [
                    0,
                    1
                ]
            },
            {
                "field": "urg_flag",
                "size": 1,
                "values": [
                    0,
                    1
                ]
            },
            {
                "field": "ack_flag",
                "size": 1,
                "values": [
                    0,
                    1
                ]
            },
            {
                "field": "psh_flag",
                "size": 1,
                "values": [
                    0,
                    1
                ]
            },
            {
                "field": "rst_flag",
                "size": 1,
                "values": [
                    0,
                    1
                ]
            },
            {
                "field": "syn_flag",
                "size": 1,
                "values": [
                    0,
                    1
                ]
            },
            {
                "field": "fin_flag",
                "size": 1,
                "values": [
                    0,
                    1
                ]
            }
        ]
    },
    # {
    #     "name": "windows_size",
    #     "mutations" : [
    #         {
    #             "field": "win_size",
    #             "size": 16,
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
    #             "size": 16,
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
    #             "size": 16,
    #             "values": [
    #                 0x0000,
    #                 0xFFFF
    #             ]
    #         },
    #         {
    #             "field": "urg_flag",
    #             "size": 1,
    #             "values": [
    #                 0,
    #                 1
    #             ]
    #         }
    #     ]
    # }
]

