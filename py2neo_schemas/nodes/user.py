from py2neo_schemas.nodes.notification import Notification
from root_graph_object import RootGraphObject
from py2neo.ogm import Property, Label, RelatedTo,RelatedFrom

class User(RootGraphObject): # User can also be called Learner

    activated = Label()

    login = Property()
    email = Property()
    password = Property()

    watch_video = RelatedTo("Video", "WATCH")
    search = RelatedTo("SearchInput", "SEARCH")
    like_training = RelatedTo("Training", "LIKE")
    follow_training = RelatedTo("Training", "FOLLOW")
    rate_training = RelatedTo("Training", "RATE")
    be_member = RelatedFrom("Member", "IS_USER")
    completed_lessons = RelatedTo("Lesson", "COMPLETE_LESSON")
    completed_chapters = RelatedTo("Chapter", "COMPLETE_CHAPTER")
    experiment = RelatedTo("Experience", "EXPERIMENT")
    notifications = RelatedTo("Notification", "NOTIFY")


    # def display(self):
    #     print(self.__node__)



# from py2neo import Graph
# graph = Graph(uri="bolt://localhost:7687",auth=("neo4j","1234"))
# test = "testos"
# j = Person.match(graph).where(f"_.email = '{test}'").first()
# print(j.activated)
# j.display()
# # j = Person(login="john",email=test,password="testadio",activated=True)
# # # print(j.__node__)
# # graph.push(j)
# # # # print(j.__node__)
# # # # j = Person.match(graph, "Uriel").first()
# # # # print(j)
# # # # j.display()