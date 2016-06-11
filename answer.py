#!/usr/bin/python3


import question
import user
import utils


class Answer:
    key = 0
    questionKey = 0
    userKey = 0
    answer = ""

    def __str__(self):
        return question.by_key(self.questionKey).short + ", " + self.answer + ", " + user.by_key(self.userKey).name

    def __init__(self, key, questionKey, userKey, answer):
        self.key = key
        self.questionKey = questionKey
        self.userKey = userKey
        self.answer = answer


# Helpers
def get_all():
    return utils.get_all_rows("answers", Answer)

def get(criteria, answers):
    return utils.get_items(criteria, answers)

def by_key(key):
    return get(lambda x: x.key == key, get_all())


def get_correct_answers(answers):
    return get(lambda x: correct(x), answers)



# Criteria examples
# Fix get all questions here
def correct(answer):
    return answer.answer == question.by_key(answer.questionKey).answer


def correct_answers(answer, questions):
    return answer.answer != question.get_questions(lambda x: question.get_question(x, answer.questionKey), question.get_all_questions()).answer


def get_question_answers(questionKey):
    results = []
    for answer in get_all_answers():
        if answer.questionKey == questionKey:
            results.append(answer)
    return results

def search(answerString):
    results = []
    for answer in get_all_answers():
        if answerString.lower() in answer.answer.lower():
            results.append(answer)
    return results

