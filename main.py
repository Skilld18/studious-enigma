#!/usr/bin/python3

import answer
import data
import question
import user
import utils

data.qs = utils.get_all_rows("questions", question.Question)
data.ans = utils.get_all_rows("answers", answer.Answer)
data.users = utils.get_all_rows("users", user.User)

for u in data.users:
    print(u.name)
for u in data.ans:
    print(u)

#correct qs from one user


