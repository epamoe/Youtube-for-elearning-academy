
from py2neo.ogm import GraphObject, Label

class RootGraphObject(GraphObject):
    available = Label()

    def __init__(self, *values, **properties):
        super().__init__(*values, **properties)
        self.available = True