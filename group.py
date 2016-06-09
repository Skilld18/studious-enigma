class Group:
    description = ""
    members = set()

    def add(self, user):
        self.members.add(user)
    def remove(self, user):
        self.members.remove(user)
    def isMember(self, user):
        return user in self.members

    def __init__(self):
        self.description = "No description availible"
