#!/usr/bin/python3
"""Module contains class_to_json function"""


def class_to_json(obj):
    """
    Dictionary description with simple data structure

    Args:
        obj: Pytho object

    Returns:
        Returns dictionary description with simple data structure
    """
    s_json = obj.__dict__

    return s_json
