#!/usr/bin/python3
import copy

import utils
# this class will have to be expanded by parsing out the tags field

all_questions = None


class Question:
    key = 0
    short = "short"
    long = "long"
    answer = "answer"
    tags = "tags"

    def __contains__(self, item):
        fields = [self.short, self.long, self.tags]
        for field in fields:
            if field is not None and item in field:
                return True

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
    global all_questions
    if not all_questions:
        all_questions = utils.get_all_rows("questions", Question)
    return copy.deepcopy(all_questions)


def get(criteria, questions):
    return utils.get_items(criteria, questions)


def by_key(key):
    for question in get(lambda x: x.key == key, get_all()):
        return question


def search(string, answers):
    return get(lambda x: string in x, answers)

