#!/usr/bin/env python


import copy

import utils

# Stores all users
all_users = None


class User:
    key = 1
    name = "UsEr"

    def __str__(self):
        return self.name

    def __init__(self, key, name):
        self.key = key
        self.name = name


def get_all():
    global all_users
    if not all_users:
        all_users = utils.get_all_rows("users", User)
    return copy.deepcopy(all_users)


def get(criteria, users):
    return utils.get_items(criteria, users)


def by_key(key):
    for question in get(lambda x: x.key == key, get_all()):
        return question


def my_answers(user_key, all_answers):
    return get(lambda x: x.user_key == user_key, all_answers)
