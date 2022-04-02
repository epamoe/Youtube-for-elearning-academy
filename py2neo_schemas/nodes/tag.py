from py2neo.ogm import Property, RelatedFrom
from py2neo_schemas.nodes.root_graph_object import RootGraphObject

class Tag(RootGraphObject):
    
    content = Property()

    training_described = RelatedFrom("Training","DESCRIBE")