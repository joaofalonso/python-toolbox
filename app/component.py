
class Component():

    def set_component_type(self):
        return type(self.value)
    
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.type = self.set_component_type()