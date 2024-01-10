#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value

    Args:
        a_dictionary: dictionary

    Return:
          key: string
    """
    if not a_dictionary:
        return None

    my_key = ""
    max_checker = 0

    for kp, vp in a_dictionary.items():
        if max_checker < vp:
            max_checker = vp
            my_key = kp

    return my_key
