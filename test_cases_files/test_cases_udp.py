""" List with Test Cases for UPD Protocol """

test_cases = [
    {
        "name": "udp_source_port",
        "mutations" : [
            {
                "field": "udp_src_port",
                "operation": "replace",
                "values": [
                    0x0000,
                    0xFFFF
                ]
            }
        ]
    },
    {
        "name": "udp_destination_port",
        "mutations" : [
            {
                "field": "udp_dst_port",
                "operation": "replace",
                "values": [
                    0x0000,
                    0xFFFF
                ]
            }
        ]
    },
    {
        "name": "udp_length",
        "mutations" : [
            {
                "field": "udp_len",
                "operation": "replace",
                "values": [
                    0x0000,
                    0x000F,
                    0x00FF,
                    0x0FFF,
                    0xFFFF
                ]
            }
        ]
    },
    {
        "name": "udp_checksum",
        "mutations" : [
            {
                "field": "udp_checksum",
                "operation": "replace",
                "values": [
                    0x0000,
                    0xFFFF
                ]
            }
        ]
    },
    {
        "name": "trun_udp",
        "mutations": [
            {
                "field": "trun_udp",
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
