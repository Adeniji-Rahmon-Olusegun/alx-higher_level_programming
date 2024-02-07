#!/usr/bin/python3
"""Module contains load_from_json_file function"""

import json


def load_from_json_file(filename):
    """
    Creates an Object from JSON file.

    Args:
        filename: file containing JSON data

    Return:
        None
    """
    with open(filename, mode="r") as json_file:
        json.load(json_file)
