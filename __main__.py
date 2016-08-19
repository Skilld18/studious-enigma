#!/usr/bin/env python
import configparser
import os

import argparse

from studious import answer, question, user, utils, version

if __name__ == "__main__":

    # Config File for username, password? and settings
    config = configparser.ConfigParser()

    if not os.path.isfile('.studiousrc'):
        config['USER'] = {'name': input("Please enter a username: ")}
        with open('.studiousrc', 'w') as configfile:
            config.write(configfile)
        exit(0)

    config.read('.studiousrc')

    if not user.exists(config['USER']["name"]):
        user.add(config['USER']['name'])

    me = user.exists(config['USER']['name']).__next__()

    parser = argparse.ArgumentParser()

    # This sorts the type of command
    parser.add_argument("--version", default=False, action="store_true", help="prints the version number")
    parser.add_argument("-question", default=False, action="store_true", help="search questions")
    parser.add_argument("-answer", default=False, action="store_true", help="search answer")
    parser.add_argument("-user", default=False, action="store_true", help="search user")
    parser.add_argument("-group", default=False, action="store_true", help="search group")
    # if none of the above assume answering a question?

    # Any given command can filter the set of data it acts on
    parser.add_argument('commands', nargs='*', default="")

    # Verbose debug flag
    parser.add_argument("-verbose", default=False, action="store_true", help="verbose")

    args = parser.parse_args()

    if args.version:
        print(version.__name__ + " version " + version.__version__)

    elif args.question:
        # apply filter
        if len(args.commands)>=2:
            # TODO:: return and print question
            utils.update_answer(int(args.commands[0]), me.key, args.commands[1])
        else:
            for q in question.get_all():
                print(q)
            #TODO: print by filter


    # TODO: mark correct
    # TODO: aggregate report
    elif args.answer:
        for a in answer.get(lambda x: x.user_key == me.key):
            print(a)
        # for ans in answer.get(lambda x: x.user_key == me[0][0]):
        #     print(ans)

    elif args.group:
        print("Group")

    elif args.user:
        print("User")

    else:
        print("Help")

        # print("\nUser answers")
        # for ans in (user.my_answers(1, answer.get_all())):):):
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
