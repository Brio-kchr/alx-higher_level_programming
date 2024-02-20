#!/usr/bin/python3


"""function that deletes a key value pair"""


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
