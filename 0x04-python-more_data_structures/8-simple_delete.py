#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Deleted a key in a dictionary

    Args:
        a_dictionary: dictionary
        key: string
        value: string/float/int/char

    Return:
          Dictionary
    """
    if key not in a_dictionary:
        pass
    else:
        del a_dictionary[key]

    return a_dictionary
