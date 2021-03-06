#!/usr/bin/python3
import argparse
import configparser
import os

from studious import answer, interactive, question, user, utils, version

if __name__ == "__main__":

    # Config File for username, password? and settings
    config = configparser.ConfigParser()

    if not os.path.isfile('.studiousrc'):
        config['USER'] = {'name': input("Please enter a username: ")}
        with open('.studiousrc', 'w') as configfile:
            config.write(configfile)

    config.read('.studiousrc')

    if not user.exists(config['USER']["name"]):
        user.add(config['USER']['name'])

    me = user.User(0, "Test")
    name = config['USER']['name']
    for e in user.exists(name):
        me = e


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

    criteria = ""
    if len(args.commands) > 0:
        criteria = args.commands[0]

    if args.version:
        print(version.__name__ + " version " + version.__version__)

    elif args.question:
        if criteria.isdigit():
            q = question.by_key(int(criteria))
            if q:
                print(q)
                if len(args.commands) > 1:
                    utils.update_answer(1, 12, args.commands[1])
                    print("My answer is " + str(args.commands[1]))
            else:
                print("No questions with key " + criteria)
        else:
            # TODO: Add logic to answers
            for q in utils.search(criteria, question.get_all()):
                print(q)



    # TODO: mark correct
    # TODO: aggregate report
    elif args.answer:
        for a in answer.get(lambda x: x.user_key == me.key):
            print(a.__str__(args.verbose) + ("Correct" if a.correct() else "Incorrect"))

    elif args.group:
        print("Group")

    elif args.user:
        print(me)

    else:
        interactive.interact(me)
        # print("To view answers use the -answer flag ex. \"python __main__.py -answers\"\n"
        #       "To view questions use the -question flag ex. \"python __main__.py -questions\"\n"
        #       "To answer questions use the question flag, select a question and an answer ex. \n"
        #       "\"python __main__.py -questions 1 answer\n"
        #       "\"python __main__.py -questions math nine answer\"")
