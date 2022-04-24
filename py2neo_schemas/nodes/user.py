# from root_graph_object import RootGraphObject
from py2neo.ogm import Property, Label, RelatedTo,RelatedFrom,GraphObject
from py2neo_schemas.nodes.application import Application
from py2neo_schemas.nodes.notification import Notification

from py2neo_schemas.nodes.root_graph_object import RootGraphObject

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
    application = RelatedTo("User", "APPLY")

    def apply(self):
        application = Application(status=Application.PENDING)
        self.application.add(application)


    # def display(self):
    #     print(self.__node__)



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