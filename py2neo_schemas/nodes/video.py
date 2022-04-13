from turtle import title
from py2neo.ogm import GraphObject, Property,RelatedFrom,RelatedTo
from py2neo_schemas.nodes.root_graph_object import RootGraphObject

class Video(RootGraphObject):

    video_id = Property()
    title = Property()
    viewCount = Property()
    channel_name = Property()
    channel_id = Property()
    published_at = Property()
    description = Property()
    subtitles = Property()

    gathered_by = RelatedFrom("Lesson","GATHER")
    watched_by = RelatedFrom("User","WATCH")