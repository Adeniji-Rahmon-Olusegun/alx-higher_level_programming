#!/usr/bin/python3
"""Module contains from_json_string function"""

import json


def to_json_string(my_obj):
    """
    Converts JSON string to python object

    Args:
        my_str: JSON string

    Return:
        Python object of JSON string
    """
    return json.loads(my_str)
