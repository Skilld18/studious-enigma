#!/usr/bin/python3

class Test:
    questionKey = 0
    score = 0
    description = ""

    def runPre(user):
        print("Pre")
        return 0

    def exe(user):
        print("exe")
        return 0

    def runPost(user):
        print("Post")
        return 0

    def getScore(self):
        print("getScore")
        return self.runPre() + self.exe() + self.runPost()

    def __init__(self):
        print("Test init")
