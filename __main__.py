#!/usr/bin/env python

import argparse

from studious import question, version

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--version", default=False, action="store_true", help="prints the version number")
    parser.add_argument("-question", default=False, action="store_true", help="search questions")
    parser.add_argument("-answer", default=False, action="store_true", help="search answer")
    parser.add_argument("-user", default=False, action="store_true", help="search user")
    parser.add_argument("-group", default=False, action="store_true", help="search group")

    parser.add_argument("-verbose", default=False, action="store_true", help="verbose")

    # Questions user has/hasn't answered

    args = parser.parse_args()
    if args.version:
        print(version.__name__ + " version " + version.__version__)
        exit(0)
    if args.question:
        if args.verbose:
            for q in question.get_all():
                print(q.verbose())
        else:
            for q in question.get_all():
                print(q)

    # print("\nCorrect answers")
    # for ans in answer.get_correct_answers(answer.get_all()):
    #     print(ans)
    #
    # print("\nUser answers")
    # for ans in (user.my_answers(1, answer.get_all())):
    #     print(ans)
    #
    # print("\nCorrect from a given user")
    # for ans in answer.get_correct_answers(user.my_answers(1, answer.get_all())):
    #     print(ans)
    #
    # print("\nQuestion contains string + 9")
    # for ans in question.search("+ 9", question.get_all()):
    #     print(ans)
    #
    # # This shouldn't be directly using keys
    # print("\nStudent 1 changes answer to question 1 to 42")
    # utils.update_answer(1, 1, "42")

