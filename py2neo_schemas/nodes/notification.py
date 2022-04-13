from py2neo.ogm import Property, RelatedFrom,GraphObject

class Notification(GraphObject):
    content = Property()

    user = RelatedFrom("User", "NOTIFY")