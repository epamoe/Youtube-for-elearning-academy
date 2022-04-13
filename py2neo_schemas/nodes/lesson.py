from py2neo.ogm import GraphObject, Property, RelatedFrom,RelatedTo
from py2neo_schemas.nodes.root_graph_object import RootGraphObject

class Lesson(RootGraphObject):
    title = Property()
    rank_nb = Property()
    
    subdivided = RelatedFrom("Chapter","SUBDIVIDE")
    gather = RelatedTo("Video","GATHER")
    user_completed = RelatedFrom("User","COMPLETE_LESSON")