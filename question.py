#!/usr/bin/python3

# this class will have to be expanded by parsing out the tags field

class Question:
    key = 0
    short = "short"
    long = "long"
    answer = "answer"
    tags = "tags"

    def __str__(self):
        return self.short

    def __init__(self, key, short, long, answer, tags):
        self.key = key
        self. short = short
        self.long = long
        self. answer = answer
        self.tags = tags


# Helpers

# Criteria
