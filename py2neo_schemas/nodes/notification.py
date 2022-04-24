from py2neo.ogm import Property,RelatedFrom
from py2neo_schemas.nodes.root_graph_object import RootGraphObject

class Notification(RootGraphObject):
    
    content = Property()
    status = Property()

    user_notified = RelatedFrom("User","NOTIFY")