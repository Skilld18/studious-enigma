#!/usr/bin/python3
import answer
import question

print(question.search('ipsum')[0].long)
print(answer.search('ello')[0].answer)
for answer in answer.get_all_answers():
    print(answer.answer)





