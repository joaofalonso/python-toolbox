import unittest
from app import convert_to_dict, myparse_json
from json import JSONDecodeError

test_json_source = '{"name":"user", "last_name" : "user_last_name"}'

class TestClass(unittest.TestCase):

    def test_convert_str_to_dict_success(self):
        result = convert_to_dict(test_json_source)
        self.assertEqual(type(result), dict)

    def test_convert_str_to_dict_jsdecode_error(self):
        json_value = '\{"name":"value"}'
        self.assertRaises(JSONDecodeError, convert_to_dict, json_value)

    def test_parse_to_component_success(self):
        result = myparse_json(test_json_source)
        self.assertEqual(len(result) , 2)

    def test_parse_to_component_jsdecode_error(self):
        json_value = '\{"name":"value"}'
        self.assertRaises(JSONDecodeError, myparse_json, json_value)