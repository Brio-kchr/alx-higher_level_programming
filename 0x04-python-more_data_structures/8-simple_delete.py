#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Function for deleting a value from a dict

    Args:
        a_dictionary: the dictionary to be updated
        key: The key of the element to be deleted

    Returns:
        The dictionary without the deleted key
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
