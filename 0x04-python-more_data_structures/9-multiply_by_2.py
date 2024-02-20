#!/usr/bin/python3


"""function that returns a new dictionary with all values multiplied by 2"""


def multiply_by_2(a_dictionary):
    'Create a new dict store doubled values'
    new_dict = dict()
    'Loop through your dict, double each value
    and update our new dict'
    for key, value in a_dictionary.items():
        new_dict.update({key: value*2})
    return new_dict
