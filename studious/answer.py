#!/usr/bin/env python

import copy

from studious import question, user, utils

all_answers = None


class Answer:
    key = 0
    question_key = 0
    user_key = 0
    answer = ""

    def __contains__(self, item):
        return item in self.answer

    def __str__(self):
        return question.by_key(self.question_key).short + ", " + self.answer + ", " + user.by_key(self.user_key).name

    def __init__(self, key, question_key, user_key, answer):
        self.key = key
        self.question_key = question_key
        self.user_key = user_key
        self.answer = answer

    # Criteria examples
    def correct(self):
        return self.answer == question.by_key(self.question_key).answer

    # Operations
    def update(self):
        utils.update_answer(self.key, self.question_key, self.answer)


# Helpers
def get_all():
    global all_answers
    if not all_answers:
        all_answers = utils.get_all_rows("answers", Answer)
    return copy.deepcopy(all_answers)


def get(criteria, answers=get_all()):
    return utils.get_items(criteria, answers)


def by_key(key):
    return get(lambda x: x.key == key, get_all())


# More human helpers
# Should maybe default answers to the whole set of the data
def get_correct_answers(answers):
    return get(lambda x: x.correct(), answers)


def search(string, answers):
    return get(lambda x: x.contains(string), answers)



