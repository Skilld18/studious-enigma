#!/usr/bin/env python

import argparse

# get set of questions
# if set contains one you can answer with next argument
# if set contains one q with no answer stdin can answer
# if stdin is file run code?

from studious import answer, utils, question, user, version

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--version", default=False, action="store_true", help="prints the version number")
    parser.add_argument("--zebra", default=False, action="store_true", help="Zebra")

    args = parser.parse_args()
    if args.version:
        print(version.__name__ + " version " + version.__version__)
        exit(0)

    if args.zebra:
        print("Zebra")
        exit(0)

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
    print("\nStudent 1 changes answer to question 1 to 42")
    utils.update_answer(1, 1, "42")
