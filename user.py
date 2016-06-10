#!/usr/bin/python3
import utils


class User:

    key = 1
    name = "UsEr"
    answers = []

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


    def __init__(self, name):
        self.name = name
