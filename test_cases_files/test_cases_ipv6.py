""" List with Test Cases for IPv6 Protocol """

test_cases = [
    {
        "name": "ip_version_ipv6",
        "mutations" : [
            {
                "field": "ipv6_version",
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
        "name": "traffic_class",
        "mutations" : [
            {
                "field": "traffic_class",
                "operation": "replace",
                "values": [
                    0x00,
                    0x01,
                    0x02,
                    0x03,
                    0xFC,
                    0xFD,
                    0xFE,
                    0xFF
                ]
            }
        ]
    },
    {
        "name": "flow_label",
        "mutations" : [
            {
                "field": "flow_label",
                "operation": "replace",
                "values": [
                    0x000000,
                    0x03FFFF
                ]
            }
        ]
    },
    {
        "name": "payload_length",
        "mutations" : [
            {
                "field": "payload_length",
                "operation": "replace",
                "values": [
                    0x0000,
                    0xFFFF
                ]
            }
        ]
    },
    {
        "name": "next_header",
        "mutations" : [
            {
                "field": "next_header",
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
        "name": "hop_limit",
        "mutations" : [
            {
                "field": "hop_limit",
                "operation": "replace",
                "values": [
                    0x00,
                    0xFF
                ]
            }
        ]
    },
    {
        "name": "source_address_IPv6",
        "mutations" : [
            {
                "field": "src_addr_ipv6",
                "operation": "replace",
                "values": [
                    0x00000000000000000000000000000000,
                    0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
                ]
            }
        ]
    },
    {
        "name": "destination_address_IPv6",
        "mutations" : [
            {
                "field": "dst_addr_ipv6",
                "operation": "replace",
                "values": [
                    0x00000000000000000000000000000000,
                    0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
                ]
            }
        ]
    }
]

