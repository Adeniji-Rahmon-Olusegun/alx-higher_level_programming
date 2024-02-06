#!/usr/bin/python3
"""Module contains to_json_string function"""

import json


def to_json_string(my_obj):
    """
    Converts string object to json

    Args:
        my_obj: string object

    Return:
        Json representation of string
    """
    return json.dumps(my_obj)
