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
        return utils.get_by_key(self.questionKey,utils.get_all_rows("questions", question.Question)).short + ", " + \
            self.answer + ", " + utils.get_by_key(self.userKey, utils.get_all_rows("users", user.User)).name

    def __init__(self, key, questionKey, userKey, answer):
        self.key = key
        self.questionKey = questionKey
        self.userKey = userKey
        self.answer = answer


def get_all_answers():
    return utils.get_all_rows("answers", Answer)

def get_answers(criteria, answers):
    return filter(criteria, answers)


# Helpers

def get_correct_answers(answers):
    return get_answers(lambda x: correct(x), answers)


# Criteria examples
#fix get all questions here
def correct(answer):
    return answer.answer == question.get_question_by_key(question.get_all_questions(), answer.key)


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

