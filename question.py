#!/usr/bin/python3

import utils

# this class will have to be expanded by parsing out the tags field
class Question:
    key = 0
    short = "short"
    long = "long"
    answer = "answer"
    tags = "tags"

    def __init__(self, key, short, long, answer, tags):
        self.key = key
        self. short = short
        self.long = long
        self. answer = answer
        self.tags = tags


def get_all_questions():
    return utils.get_all_rows("questions", Question)

def get_questions(criteria):
    return filter(criteria, get_all_questions())

# Example criteria function
def search(question, string):
    return any(map(lambda x: x is not None and string in x, [question.short, question.long, question.tags]))


