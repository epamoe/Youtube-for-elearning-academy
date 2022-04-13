from py2neo.ogm import Property, RelatedFrom, GraphObject

class Domain(GraphObject):
    
    content = Property()

    trainings = RelatedFrom("Training", "BELONG")