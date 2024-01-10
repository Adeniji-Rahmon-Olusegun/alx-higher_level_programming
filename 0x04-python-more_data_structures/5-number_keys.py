#!/usr/bin/python3

def number_keys(a_dictionary):
    """
    Returns the number of keys in a dictionary

    Args:
        a_dictionar: dictionary

    Return:
          integer

    """
    key_tracker = 0

    for ask_key in a_dictionary:
        key_tracker += 1

    return key_tracker
