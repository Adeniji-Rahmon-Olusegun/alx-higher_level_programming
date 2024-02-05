#!/usr/bin/python3
"""Module with  is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is of same class

    Args:
        obj: object
        a_class: secific class

    Return:
        True: if obj is of same class with  of a_class
        False: Otherwise
    """
    return isinstance(obj, a_class)
