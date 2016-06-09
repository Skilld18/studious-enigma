#!/usr/bin/python3
import group
import user

introToProg = group.Group()
ann = user.User("Alice")
introToProg.add(ann)
bob = user.User("Bob")
introToProg.add(bob)

for member in introToProg.members:
    print(member.name)

ann.answerQuestion(3, 'newqans4')




