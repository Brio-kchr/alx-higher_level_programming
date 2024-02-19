#!/usr/bin/python3


"""function that replaces all occurrences of an element by another in a new list"""

def search_replace(my_list, search, replace):
    res = [x if x != search else replace for x in my_list]
    return res
