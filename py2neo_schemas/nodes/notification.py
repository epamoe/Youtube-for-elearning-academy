from py2neo.ogm import Property,RelatedFrom
from py2neo_schemas.nodes.root_graph_object import RootGraphObject

class Notification(RootGraphObject):

    NEW_APPLICATION_TEXT = "Congratulations ! You applied to become a member. An expert will answer to your request"
    
    content = Property()
    read = Property()

    user_notified = RelatedFrom("User","NOTIFY")

    def __init__(self, *values, **properties):
        super().__init__(*values, **properties)
        self.read = False