#!/usr/bin/python3

import copy

from studious import utils

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
        return str(self.key) + ". " + self.short

    def __init__(self, key, short, long, answer, tags):
        self.key = key
        self. short = short
        self.long = long
        self. answer = answer
        self.tags = tags

    # TODO: add user answer
    def verbose(self):
        return str(self.key) + ". " + self.short + "\n" + str(self.long) + "\n" + str(self.tags)


# Helpers
def get_all():
    global all_questions
    if not all_questions:
        all_questions = utils.get_all_rows("questions", Question)
    return copy.deepcopy(all_questions)


def get(criteria, questions=get_all()):
    return utils.get_items(criteria, questions)


# TODO: is there a better way to do this with filters?
def by_key(key):
    f = list(get(lambda x: x.key == key, get_all()))
    if len(f) >= 1:
        return f[0]
    return None


def search(string, answers=get_all()):
    return get(lambda x: string in x, answers)

