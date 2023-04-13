""" List with Test Cases for IPv4 Protocol """

test_cases = [
    {
        "name": "ipv4_version",
        "mutations" : [
            {
                "field": "ipv4_version",
                "operation": "replace",
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
                "operation": "replace",
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
                "operation": "replace",
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
                "operation": "replace",
                "values": "all"
            }
        ]
    },
    {
        "name": "total_length",
        "mutations" : [
            {
                "field": "tot_len",
                "operation": "replace",
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
                "operation": "replace",
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
                "field": "rsv_flag",
                "operation": "replace",
                "values": "all"
            },
            {
                "field": "df_flag",
                "operation": "replace",
                "values": "all"
            },
            {
                "field": "mf_flag",
                "operation": "replace",
                "values": "all"
            }
        ]
    },
    {
        "name": "fragment_offset",
        "mutations" : [
            {
                "field": "fragment_offset",
                "operation": "replace",
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
                "operation": "replace",
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
                "operation": "replace",
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
                "field": "ip_checksum",
                "operation": "replace",
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
                "operation": "replace",
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
                "operation": "replace",
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
        "name": "ip_option",
        "mutations" : [
            {
                "field": "ip_option",
                "operation": "insert",
                "values": [
                    "0x030400",
                    "0x03041111",
                    "0x030455030400",
                    "0x0304AAAA030400030400",
                    "0x0304FF030400030400030400",
                    "0x03040000",
                    "0x030411030400",
                    "0x03035555030400030400030400030400",
                    "0x0303AA030400030400030400030400030400"
                ]
            }
        ]
    }
]

