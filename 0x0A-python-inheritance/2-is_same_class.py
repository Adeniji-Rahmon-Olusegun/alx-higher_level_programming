#!/usr/bin/python3
"""Module with  is_same_class function"""


def is_same_class(obj, a_class):
    """Checks if an object is of an instance

    Args:
        obj: object
        a_class: secific class

    Return:
        True: if obj is an instance of a_class
        False: Otherwise
    """
    return type(obj) is a_class
