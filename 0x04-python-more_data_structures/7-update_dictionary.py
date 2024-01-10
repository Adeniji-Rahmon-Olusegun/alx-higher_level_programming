#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary

    Args:
        a_dictionary: dictionary
        key: string/float/int/char
        value: string/float/int/char

    Return:
            Dictionary
    """
    a_dictionary[key] = value

    return a_dictionary
