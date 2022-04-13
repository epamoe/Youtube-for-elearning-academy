from py2neo.ogm import GraphObject, Property,RelatedFrom

class Video(GraphObject):

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