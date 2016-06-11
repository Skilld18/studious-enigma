#!/usr/bin/python3
import answer
import question
import utils

for x in utils.get_items(utils.get_all_rows("questions", question.Question), lambda y: "9" in y.short):
    print(x.short)

for q in question.get_questions(lambda x: question.search(x, "2")):
    print(q.long)


#correct qs from one user
start = utils.get_items(utils.get_all_rows("answers", answer.Answer), lambda y : y.userKey == 1)
cont = utils.get_items(start, lambda x: x.answer == question.get_question_answer(x.questionKey))
for line in cont:
    print(line.answer)


