from py2neo.ogm import Property, RelatedFrom
from py2neo_schemas.nodes.root_graph_object import RootGraphObject

class Domain(RootGraphObject):
    content = Property()

    trainings = RelatedFrom("Training", "BELONG")