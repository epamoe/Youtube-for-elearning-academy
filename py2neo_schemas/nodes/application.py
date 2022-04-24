from py2neo.ogm import Property,RelatedFrom
from py2neo_schemas.nodes.root_graph_object import RootGraphObject

class Application(RootGraphObject):

    PENDING = "pending"
    REFUSED = "refused"
    ACCEPTED = "accepted"
    
    status = Property()

    user_applying = RelatedFrom("User","APPLY")