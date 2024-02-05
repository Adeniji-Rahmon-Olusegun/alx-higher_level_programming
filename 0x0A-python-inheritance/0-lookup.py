#!/usr/bin/python3
"""Attribute and method function"""

def lookup(obj):
    """Returns the list of available attributes
    and methods of an object
    """

    return list(dir(obj))
