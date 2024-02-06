#!/usr/bin/python3
"""Module contains write_file function"""


def write_file(filename="", text=""):
    """
    Writes to a file

    Args:
        filename: file path to file
        text: data to write

    Return:
        None
    """
    with open(filename, mode="w", encoding='utf-8') as file_obj:
        file_obj.write(text)
        data_len = file_obj.tell()

    return data_len
