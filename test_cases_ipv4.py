""" List with Test Cases to generate and excecute """

test_cases = [
    {
        "name": "ip_version",
        "mutations" : [
            {
                "field": "ip_version",
                "values": [
                    0x0,
                    0x4,
                    0x6,
                    0xF
                ]
            }
        ]
    },
    {
        "name": "internet_header_length",
        "mutations" : [
            {
                "field": "ihl",
                "values": [
                    0x0,
                    0x8,
                    0xF
                ]
            }
        ]
    },
    {
        "name": "differentiated_services_code_point",
        "mutations" : [
            {
                "field": "dscp",
                "values": [
                    0x00,
                    0xFC,
                ]
            }
        ]
    },
    {
        "name": "explicit_congestion_notification",
        "mutations" : [
            {
                "field": "ecn",
                "values": "all"
            }
        ]
    },
    {
        "name": "total_length",
        "mutations" : [
            {
                "field": "tot_len",
                "values": [
                    0x0000,
                    0x003F,
                    0x009F,
                    0xFFFF
                ]
            }
        ]
    },
    {
        "name": "identification",
        "mutations" : [
            {
                "field": "iden",
                "values": [
                    0x0000,
                    0xFFFF
                ]
            }
        ]
    },
    {
        "name": "ip_flags",
        "mutations" : [
            {
                "field": "flags",
                "values": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ]
            }
        ]
    },
    {
        "name": "fragment_offset",
        "mutations" : [
            {
                "field": "fragment_offset",
                "values": [
                    0x0000,
                    0x00F0,
                    0x1FFF
                ]
            }
        ]
    },
    {
        "name": "time_to_live",
        "mutations" : [
            {
                "field": "time_to_live",
                "values": [
                    0x00,
                    0xFF
                ]
            }
        ]
    },
    {
        "name": "protocol",
        "mutations" : [
            {
                "field": "protocol",
                "values": [
                    0x00,
                    0x06,
                    0x11,
                    0xFF
                ]
            }
        ]
    },
    {
        "name": "ip_checksum",
        "mutations" : [
            {
                "field": "checksum",
                "values": [
                    0x0000,
                    0xFFFF
                ]
            }
        ]
    },
    {
        "name": "source_address",
        "mutations" : [
            {
                "field": "src_addr",
                "values": [
                    0x00000000,
                    0xFFFFFFFF,
                    0x7D004B00,
                    0x7D004BFF,
                    0x7D004B30,
                    0x78004B30,
                    0x78004B00,
                    0x78004BFF
                ]
            }
        ]
    },
        {
        "name": "destiantion_address",
        "mutations" : [
            {
                "field": "dst_addr",
                "values": [
                    0x00000000,
                    0xFFFFFFFF,
                    0x7D004B00,
                    0x7D004BFF,
                    0x7D004B30,
                    0x78004B30,
                    0x78004B00,
                    0x78004BFF
                ]
            }
        ]
    }
]

