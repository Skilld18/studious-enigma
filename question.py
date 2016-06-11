#!/usr/bin/python3
import utils
# this class will have to be expanded by parsing out the tags field

class Question:
    key = 0
    short = "short"
    long = "long"
    answer = "answer"
    tags = "tags"

    def __str__(self):
        return self.short

    def __init__(self, key, short, long, answer, tags):
        self.key = key
        self. short = short
        self.long = long
        self. answer = answer
        self.tags = tags


# Helpers
def get_all():
    return utils.get_all_rows("questions", Question)

def get(criteria, questions):
    return utils.get_items(criteria, questions)

def by_key(key):
    for question in get(lambda x: x.key == key, get_all()):
        return question


# Criteria
