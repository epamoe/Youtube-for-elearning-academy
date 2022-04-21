from py2neo.ogm import Property,RelatedFrom
from py2neo_schemas.nodes.root_graph_object import RootGraphObject

class Technology(RootGraphObject):
    
    content = Property()

    training_using = RelatedFrom("Training","USE")