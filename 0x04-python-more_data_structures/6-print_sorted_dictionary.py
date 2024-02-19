#!/usr/bin/python3


"""function that prints a dict by ordered keys"""


def print_sorted_dictionary(a_dictionary):
    if type(a_dictionary) is dict:
        for x, y in sorted(a_dictionary.items()):
            print("{} : {}".format(x, y))
