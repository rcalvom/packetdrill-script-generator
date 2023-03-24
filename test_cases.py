""" List with Test Cases to generate and excecute """

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
    }
]

