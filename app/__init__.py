import json
from app.component import Component

def myparse_json(json_value):

    value_dict = json_value
    if (json_value and (type(json_value) == str)):       
        value_dict = json.loads(json_value)
    return map_values(value_dict)
    

def map_values(dict, components = None):
    if not components:
        components = []

    for k, v in dict.items():
        if type(v) == dict:
            map_values(v, components)
        else:
            components.append(Component(k, v))
    return components