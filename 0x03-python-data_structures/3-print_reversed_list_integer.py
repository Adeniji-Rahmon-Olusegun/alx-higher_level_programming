#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Prints all integers in a list in reverse order

    Args:
        my_list: list of elements

    Return:
            None
    """
    if (my_list):
        for obj in range(len(my_list) - 1, -1, -1):
            print("{:d}".format(my_list[obj]))
