from py2neo.ogm import Property,RelatedFrom
from py2neo_schemas.nodes.root_graph_object import RootGraphObject

class Application(RootGraphObject):
    
    status = Property()

    user_applying = RelatedFrom("User","APPLY")