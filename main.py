#!/usr/bin/python3
import question


for q in question.get_questions(lambda x: question.search(x, "2")):
    print(q.long)





