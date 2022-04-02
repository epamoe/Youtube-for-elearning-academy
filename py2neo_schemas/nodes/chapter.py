from py2neo.ogm import GraphObject, Property, RelatedFrom,RelatedTo
from py2neo_schemas.nodes.root_graph_object import RootGraphObject

class Chapter(RootGraphObject):
        
    title = Property()

    contained_by = RelatedFrom("Training","CONTAIN")
    subdivide = RelatedTo("Lesson","SUBDIVIDE")
    user_completed = RelatedFrom("User","COMPLETE_CHAPTER")
