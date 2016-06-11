#!/usr/bin/python3

import answer
import user

print("Correct answers")
for ans in answer.get_correct_answers(answer.get_all()):
    print(ans)

print("\nUser answers")
for ans in (user.my_answers(1, answer.get_all())):
    print(ans)

print("Correct from a given user")

for ans in answer.get_correct_answers(user.my_answers(1, answer.get_all())):
    print(ans)

