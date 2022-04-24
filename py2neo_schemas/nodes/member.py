from py2neo.ogm import RelatedFrom, RelatedTo
from py2neo_schemas.nodes.root_graph_object import RootGraphObject

class Member(RootGraphObject): # Member can also be called Expert
    
    user = RelatedFrom("User", "IS_MEMBER")
    published_trainings = RelatedTo("Training", "PUBLISH")

