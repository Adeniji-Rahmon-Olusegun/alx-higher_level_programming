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
    with open(filename, 'r', encoding='utf-8') as file_obj:
        for data_txt in file_obj:
            print(data_txt, end="")
