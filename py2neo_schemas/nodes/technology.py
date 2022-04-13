from py2neo.ogm import Property,RelatedFrom,GraphObject

class Technology(GraphObject):
    
    content = Property()

    training_using = RelatedFrom("Training","USE")