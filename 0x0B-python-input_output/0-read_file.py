#!/usr/bin/python3
"""This module contains read_file function"""


def read_file(filename=""):
    """
    Reads a text file

    Args:
        filename: file path

    Return:
        None
    """
    with open(filename, "r") as file_obj:
        print(file_obj.read())
