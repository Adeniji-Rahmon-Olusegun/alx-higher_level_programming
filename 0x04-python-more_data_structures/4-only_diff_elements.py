#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set

    Args:
        set_1: set
        Set_2: set

    Return:
          set
    """
    return set_1.union(set_2) - set_1.intersection(set_2)
