from inspect import stack
from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo
from py2neo_schemas.nodes.root_graph_object import RootGraphObject

class Training(RootGraphObject):
    title = Property()
    follower_nbr = Property()
    description = Property()
    mark = Property()
    thumbnail = Property()

    users_liking = RelatedFrom("User","LIKE")
    users_following = RelatedFrom("User","FOLLOW")
    users_rating = RelatedFrom("User","RATE")
    publisher = RelatedFrom("Member","PUBLISH")
    domain = RelatedTo("Domain", "BELONG")
    tags = RelatedTo("Tag", "DESCRIBE")
    stack = RelatedTo("Technology", "USE")
    chapters = RelatedTo("Chapter", "CONTAIN")
