#!/usr/bin/python3
"""Module contains append_write function"""


def append_write(filename="", text=""):
    """
    Appends data to a file

    Args:
        filename: path containing the file
        text: data to be appended
    Return:
        Number of characters appended
    """
    with open(filename, mode="a", encoding="utf-8") as file_obj:
        data_len = file_obj.write(text)

    return data_len
