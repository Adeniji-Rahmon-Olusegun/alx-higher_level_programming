#!/urs/bin/python3
"""Module contains inherits_from function"""


def inherits_from(obj, a_class):
    """Checks if an object is a subclass of aparent class

    Args:
        obj: Object
        a_class: Assumed Parent class

    Return:
        True: if obj is subclass of a_class
        False: otherwise
    """
    if issubclass(type(obj), a_class):
        return type(obj) != a_class
    return False
