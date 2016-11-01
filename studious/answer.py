#!/usr/bin/env python

import copy

from studious import question, utils

all_answers = None


class Answer:
    key = 0
    question_key = 0
    user_key = 0
    answer = ""

    def __contains__(self, item):
        return item in self.answer

    def __str__(self, verbose=False):
        if not verbose:
            return str(question.by_key(self.question_key)) + ", " + self.answer + ", "
        return str(self.key) + ", " + str(self.question_key) + ", " + str(self.user_key) + ", " + self.answer + ", "

    def __init__(self, key, question_key, user_key, answer):
        self.key = key
        self.question_key = question_key
        self.user_key = user_key
        self.answer = answer

    def __cmp__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key
    # Criteria examples
    # TODO:: Need a better way to eval correct
    def correct(self):
        return self.answer == question.by_key(self.question_key).answer

    def is_users(self, user):
        return self.user_key == user

    # Operations
    def update(self):
        utils.update_answer(self.key, self.question_key, self.answer)


# Helpers
def get_all():
    global all_answers
    all_answers = utils.get_all_rows("answers", Answer)
    return copy.deepcopy(all_answers)


def get(criteria, answers=get_all()):
    return utils.get_items(criteria, answers)


def by_key(key):
    return get(lambda x: x.key == key, get_all())


def get_correct_answers(answers):
    return get(lambda x: x.correct(), answers)

