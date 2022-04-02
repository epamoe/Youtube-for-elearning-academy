from accounts.data_classes.user import User
from py2neo.ogm import RelatedTo

class Member(User): # Member can also be called Expert
    
    user = RelatedTo("User", "IS_USER")
    published_trainings = RelatedTo("Training", "PUBLISH")

