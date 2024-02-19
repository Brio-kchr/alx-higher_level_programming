#!/usr/bin/python3


"""function that prints a dict by ordered keys"""


def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()
    for x in keys:
        print("{} : {}".format(x, a_dictionary[x]))
