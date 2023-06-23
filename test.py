import unittest
from sources.parallel_test_execution import *
from sources.generate_scripts import *
import configuration
import os


class MyTestCase(unittest.TestCase):
    
    def test_increasing_indexes(self):
        input1 = [1,2,3]
        result = increasing_indexes(input1)
        self.assertEqual(result, True)
        
        input4 = [-2, -1]
        result1 = increasing_indexes(input4)
        self.assertEqual(result1, True)
        
        input7 = [50,605,612]
        result2 = increasing_indexes(input7)
        self.assertEqual(result2, True)
        
        input2 = [-1,-2,-3]
        result3 = increasing_indexes(input2)
        self.assertEqual(result3, False)
        
        input3 = [1]
        result4 = increasing_indexes(input3)
        self.assertEqual(result4, True)
        
        input5 = [1,1,2]
        result5 = increasing_indexes(input5)
        self.assertEqual(result5, False)
    
    def test_get_available_slot(self):
        slots_1 = {1:False, 2:False, 3:False}
        my_result_1 = get_available_slot(slots_1)
        self.assertEqual(my_result_1, -1)
        
        slots_2 = {1:False, 2:True, 3:False}
        my_result_2 = get_available_slot(slots_2)
        self.assertEqual(my_result_2, 2)
        
        slots_3 = {1:True, 2:True, 3:False}
        my_result_3 = get_available_slot(slots_3)
        self.assertEqual(my_result_3, 1)
        
        slots_4 = {1:False}
        my_result_4 = get_available_slot(slots_4)
        self.assertEqual(my_result_4, -1)
        
        
    def test_create_individual_cases(self):
        test_case = {}
        test_case = {
            'name':'source_port', 
            'mutations': [
                {
                    'field':'src_port',
                    'operation':'replace',
                    'values':[
                        0, 
                        65535
                    ]
                },
                {
                    'field':'reserved',
                    'operation':'insert',
                    'values':[0]
                },
                {   
                    'field':'src_port',
                    'operation':'replace',
                    'values':[0]
                },
                {   
                    'field':'rsv_flag',
                    'operation':'truncate',
                    'values':[0]
                }
            ]
        }
         
        result_testcase = create_individual_cases(test_case)
        print(result_testcase)
        
    def test_generate_case(self):
        result = {}
        
        test_case = [
            {
                    'name': 'source_address_IPv6', 
                    'header': 'ipv6', 
                    'operation': 'replace', 
                    'field': 'src_addr', 
                    'value': '0x00000000000000000000000000000000'
            }
                    ]
        
        name = test_case[0]['name']
        templates = preload_templates(configuration.templates_filenames)
        index = 0
        
        result = generate_case(test_case, name, templates, index)
        print(result)
        
        
    def test_format_value(self):
        #Test Case 1
        value = 255
        size = 8
        
        result = format_value(value, size)
        # print(result)
        self.assertEqual(result, '0xFF')
        
        # #Test Case 2 - Case when value is 0:        
        value = 0
        size = 8

        result = format_value(value, size)
        # print(result)  # Expected output: 0x00
        self.assertEqual(result, '0x00')
        
        #Test Case 3 - Case when size is not a multiple of 8:
        value = 1024
        size = 12

        result = format_value(value, size)
        # print(result)  # Expected output: 0x100
        self.assertEqual(result, '0x0400')

        #Test Case 4 - Case when value is the maximum value for the given size:
        value = (2 ** 24) - 1  # Maximum value for 24 bits
        size = 24

        result = format_value(value, size)
        # print(result)  # Expected output: 0xFFFFFF
        self.assertEqual(result, '0xFFFFFF')

        #Test Case 5 - Case when size is smaller than the number of bits required to represent value:
        value = 1024
        size = 4

        result = format_value(value, size)
        # print(result)  # Expected output: 0x400
        self.assertEqual(result, '0x400')
        
        #Test Case 6 - Case when size is a multiple of 8:
        value = 1024
        size = 16

        result = format_value(value, size)
        # print(result)  # Expected output: 0x0400
        self.assertEqual(result, '0x0400')
    
    def test_generate_expression(self):
        
        test_case1 = [{'name': 'source_address_IPv6', 
                       'header': 'ipv6', 
                       'operation': 'replace', 
                       'field': 'src_addr', 
                       'value': '0x00000000000000000000000000000000'
                       }
                      ]

        result = generate_expresion(test_case1)
        print(result)
        

    def test_generate_scripts(self):
        
        configuration.k = 2
        
        err_count = 0
        known_scripts = []
        generated_scripts = []
        
        scripts_folder_path = './scripts'
        sample_script_folder_path = './sample_scripts'
        
        for script_name in os.listdir(sample_script_folder_path):
            file_path = os.path.join(sample_script_folder_path, script_name)
            if os.path.isfile(file_path):
                known_scripts.append(script_name)
                
        generate_scripts(test_cases, configuration.templates_filenames)
        
        for script in os.listdir(scripts_folder_path):
            file_path_gen = os.path.join(scripts_folder_path, script)
            if os.path.isfile(file_path_gen):
                generated_scripts.append(script)
            
        for i in known_scripts:
            for j in generated_scripts:
                
                if i == j:   
                    with open(os.path.join(sample_script_folder_path, i), 'r') as f1, open(os.path.join(scripts_folder_path, j), 'r') as f2:
                        
                       content1 = f1.read()
                       content2 = f2.read()
                       
                       if content1 != content2:
                           err_count += 1
                           
        self.assertEqual(err_count, 0)
        
        # self.assertGreater(len(generated_scripts),)
        
    # def test_generate_scripts(self):
    
    #     configuration.k = 1
    #     self.test_scripts()
        
    #     configuration.k = 2
    #     self.test_scripts()
            