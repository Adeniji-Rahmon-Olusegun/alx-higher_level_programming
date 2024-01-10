#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values
    multiplied by 2

    Args:
        a_dictionary: dictionary

    Return:
          Dictionary
    """
    mod_dict = a_dictionary.copy()

    for itm_d in mod_dict:
        mod_dict[itm_d] = mod_dict[itm_d] * 2

    return mod_dict
