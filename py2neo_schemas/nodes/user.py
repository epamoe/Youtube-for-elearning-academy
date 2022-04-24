# from root_graph_object import RootGraphObject
from py2neo.ogm import Property, Label, RelatedTo,RelatedFrom,GraphObject
from py2neo_schemas.nodes.application import Application
from py2neo_schemas.nodes.notification import Notification

from py2neo_schemas.nodes.root_graph_object import RootGraphObject
from db_graph import graph


class User(RootGraphObject): # User can also be called Learner 
    __primarykey__ = 'login'

    activated = Label()

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

# graph = Graph(uri="bolt://localhost:7687",auth=("neo4j","1234"))
# test = "testos"
# j = Person.match(graph).where(f"_.email = '{test}'").first()
# print(j.activated)
# j.display()
# # j = Person(login="urielle",email=test,password="testadio",activated=True)
# # # print(j.__node__)
# # graph.push(j)
# # # # print(j.__node__)
# # # # j = Person.match(graph, "Uriel").first()
# # # # print(j)
# # # # j.display()