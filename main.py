#!/usr/bin/python3

import answer
import question
import user
import utils


print("\nCorrect answers")
for ans in answer.get_correct_answers(answer.get_all()):
    print(ans)

print("\nUser answers")
for ans in (user.my_answers(1, answer.get_all())):
    print(ans)

print("\nCorrect from a given user")
for ans in answer.get_correct_answers(user.my_answers(1, answer.get_all())):
    print(ans)

print("\nQuestion contains string + 9")
for ans in question.search("+ 9", question.get_all()):
    print(ans)

# This shouldn't be directly using keys
print("\nStudent 0 changes answer to question 1 to 42")
utils.update_answer(1, 1, "42")



