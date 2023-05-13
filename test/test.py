import unittest
from app import myparse_json
from json import JSONDecodeError

class TestClass(unittest.TestCase):

    def test_parse_string_to_dict_sucess(self):
        json_value = '{"name":"value"}'
        dict = myparse_json(json_value)
        self.assertEqual(len(dict), 1)

    def test_parse_string_to_dict_error(self):
        json_value = '\{"name":"value"}'
        self.assertRaises(JSONDecodeError, myparse_json, json_value)