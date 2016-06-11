#!/usr/bin/python3

import utils


class User:
    key = 1
    name = "UsEr"

    def __str__(self):
        return self.name

    def answerQuestion(self, questionKey, answerString):
        conn = utils.getConn()
        cur =  conn.cursor()
        data = (str(self.key),str(questionKey),answerString)
        cur.execute("""
        INSERT INTO answers(key, questionKey, userKey, answer)
        VALUES (DEFAULT ,%s,%s,%s)
        ON CONFLICT (questionKey, userKey) DO UPDATE SET answer = EXCLUDED.answer;
        """, data)
        conn.commit()

        cur.execute("SELECT * FROM answers")
        for row in cur.fetchall():
            print(row)

        cur.close()
    #not sure if this is ever nescesary or even if it should ever get called
    def removeAnswer(self, question):
        self.answers.remove(1)


    def __init__(self, key, name):
        self.key = key
        self.name = name


def get_all():
    return utils.get_all_rows("users", User)

def get(criteria, users):
    return utils.get_items(criteria, users)

def by_key(key):
    for user in get(lambda x: x.key == key, get_all()):
        return user


def my_answers(userKey, all_answers):
    return get(lambda x: x.userKey == userKey, all_answers)
