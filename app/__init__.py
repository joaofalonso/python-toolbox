import json
from app.component import Component

def convert_to_dict(json_value):
    return json.loads(json_value)

def myparse_json(json_value):
    dict = convert_to_dict(json_value)
    return map_values(dict)
    

def map_values(dict, components = None):
    if not components:
        components = []

    for k, v in dict.items():
        if type(v) == dict:
            map_values(v, components)
        else:
            components.append(Component(k, v))
    return components