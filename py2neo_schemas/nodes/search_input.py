from py2neo.ogm import Property,RelatedFrom,GraphObject

class SearchInput(GraphObject):

    content = Property()

    searched_by = RelatedFrom("User","SEARCH")
