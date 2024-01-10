#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """
    Deletes keys with a specific value in a dictionary

    Args:
        a_dictionary: dictionary
        value: str/int/float

    Return:
          Dictionary
    """
    key_population = [k for k, v in a_dictionary.items() if v == value]

    for k_del in key_population:
        del a_dictionary[k_del]

    return a_dictionary
