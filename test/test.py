import unittest
from app import myparse_json
from json import JSONDecodeError
from app.component import Component

test_json_source = '{"name":"user", "last_name" : "user_last_name", "age": 30, "active" : true}'

class TestParser(unittest.TestCase):

    def test_parse_to_component_success(self):
        result = myparse_json(test_json_source)
        name_component = result[0]

        self.assertEqual(len(result) , 4)
        self.assertEqual(type(name_component), Component)
        self.assertEqual(name_component.type, str)

        age_component = result[2]
        self.assertEqual(age_component.type, int)
        
        active_component = result[3]
        self.assertEqual(active_component.type, bool)

    def test_parse_to_component_jsdecode_error(self):
        json_value = '\{"name":"value"}'
        self.assertRaises(JSONDecodeError, myparse_json, json_value)

    