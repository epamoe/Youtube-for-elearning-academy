from py2neo.ogm import Property, RelatedFrom, GraphObject
from py2neo_schemas.nodes.root_graph_object import RootGraphObject

class Tag(GraphObject):
    
    content = Property()

    training_described = RelatedFrom("Training","DESCRIBE")