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
    questions = []
    data = utils.sql('SELECT * FROM questions')
    for row in data:
        questions.append(Question(*row))
    return questions

def search(string):
    string = string.lower()
    results = []
    for question in get_all_questions():
        fields = [question.short, question.long, question.tags]
        for field in fields:
            if field is not None and string in field:
                results.append(question)
    return results


