""" List with Test Cases to generate and excecute """

test_cases = [
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
]

