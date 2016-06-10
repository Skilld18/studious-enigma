#!/usr/bin/python3

import utils

class Answer:
    key = 0
    questionKey = 0
    userKey = 0
    answer = ""

    def __init__(self, key, questionKey, userKey, answer):
        self.key = key
        self.questionKey = questionKey
        self.userKey = userKey
        self.answer = answer


def get_all_answers():
    answers = []
    data = utils.sql('SELECT * FROM answers')
    for row in data:
        answers.append(Answer(*row))
    return answers

def get_user_answers(userKey):
    results = []
    for answer in get_all_answers():
        if answer.userKey == userKey:
            results.append(answer)
    return results

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

