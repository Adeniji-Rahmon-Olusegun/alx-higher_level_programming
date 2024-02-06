#!/usr/bin/python3
"""Module contains save_to_json_file function"""


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file using JSON repr.

    Args:
        my_obj: Python Object
        filename: file to be written to

    Return:
        None
    """
    with open(filename, mode="w") as json_file:
        json.dump(my_obj, json_file)
