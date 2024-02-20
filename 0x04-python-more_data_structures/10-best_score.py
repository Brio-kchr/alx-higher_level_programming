#!/usr/bin/python3


"""function that returns a key with the biggest integer value"""


def best_score(a_dictionary):
    if type(a_dictionary) != dict or len(a_dictionary) == 0:
        return "None"
    keys = list(a_dictionary.keys())
    values = list(a_dictionary.keys())
    max_val = max(values)
    max_key = keys[values.index(max_val)]
    return max_key
