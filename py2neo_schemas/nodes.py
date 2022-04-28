from py2neo.ogm import Property,RelatedFrom,RelatedTo, GraphObject, Label, Property
# from db_graph import graph

class RootGraphObject(GraphObject):
    available = Label()

    def __init__(self, *values, **properties):
        super().__init__(*values, **properties)
        self.available = True

class Application(RootGraphObject):

    PENDING = "pending"
    REFUSED = "refused"
    ACCEPTED = "accepted"
    
    status = Property()

    candidates = RelatedFrom("User","APPLY")

class Chapter(RootGraphObject):
        
    title = Property()
    rank_nb = Property()

    contained_by = RelatedFrom("Training","CONTAIN")
    subdivide = RelatedTo("Lesson","SUBDIVIDE")
    user_completed = RelatedFrom("User","COMPLETE_CHAPTER")

class Domain(RootGraphObject):
    
    __primarykey__ = 'content'

    content = Property()

    trainings = RelatedFrom("Training", "BELONG")


class Experience(RootGraphObject):
    
    key = Property()
    content = Property()

    user = RelatedFrom("User","EXPERIMENT")

class Lesson(RootGraphObject):
    title = Property()
    rank_nb = Property()
    
    subdivided = RelatedFrom("Chapter","SUBDIVIDE")
    gather = RelatedTo("Video","GATHER")
    user_completed = RelatedFrom("User","COMPLETE_LESSON")


class Notification(RootGraphObject):

    NEW_APPLICATION_TEXT = "Congratulations ! You applied to become a member. An expert will answer to your request"
    
    content = Property()
    read = Property()

    user_notified = RelatedFrom("User","NOTIFY")

    def __init__(self, *values, **properties):
        super().__init__(*values, **properties)
        self.read = False


class SearchInput(RootGraphObject):

    content = Property()

    searched_by = RelatedFrom("User","SEARCH")


class Tag(RootGraphObject):
    
    content = Property()

    training_described = RelatedFrom("Training","DESCRIBE")


class Technology(RootGraphObject):
    
    content = Property()

    training_using = RelatedFrom("Training","USE")


class Training(RootGraphObject):
    title = Property()
    follower_nbr = Property()
    description = Property()
    mark = Property()
    thumbnail = Property()

    users_liking = RelatedFrom("User","LIKE")
    users_following = RelatedFrom("User","FOLLOW")
    users_rating = RelatedFrom("User","RATE")
    publisher = RelatedFrom("User","PUBLISH")
    domain = RelatedTo("Domain", "BELONG")
    tags = RelatedTo("Tag", "DESCRIBE")
    stack = RelatedTo("Technology", "USE")
    chapters = RelatedTo("Chapter", "CONTAIN")


class User(RootGraphObject): # User can also be called Learner 
    __primarykey__ = 'login'

    activated = Label()
    member = Label()
    admin = Label()

    login = Property()
    email = Property()
    password = Property()

    watch_video = RelatedTo("Video", "WATCH")
    search = RelatedTo("SearchInput", "SEARCH")
    like_training = RelatedTo("Training", "LIKE")
    follow_training = RelatedTo("Training", "FOLLOW")
    rate_training = RelatedTo("Training", "RATE")
    member_node = RelatedFrom("Member", "IS_MEMBER")
    completed_lessons = RelatedTo("Lesson", "COMPLETE_LESSON")
    completed_chapters = RelatedTo("Chapter", "COMPLETE_CHAPTER")

    experiences = RelatedTo("Experience", "EXPERIMENT")
    notifications = RelatedTo("Notification", "NOTIFY")
    application = RelatedTo("Application", "APPLY")

    published_trainings = RelatedTo("Training", "PUBLISH")


    def apply(self):
        # The application node is created and linked to the user
        application = Application(status=Application.PENDING)
        self.application.add(application)
        # The notification node is created and linked to the user
        notification = Notification(content = Notification.NEW_APPLICATION_TEXT)
        self.notifications.add(notification)
    
    def did_apply(self) -> bool:
        for a in list(self.application):
            if a.available and a.status != Application.REFUSED:
                return True
        return False
    

class Video(GraphObject):

    video_id = Property()
    title = Property()
    viewCount = Property()
    channel_name = Property()
    published_at = Property()
    description = Property()
    subtitles = Property()

    gathered_by = RelatedFrom("Lesson","GATHER")
    watched_by = RelatedFrom("User","WATCH")