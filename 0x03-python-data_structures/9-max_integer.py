#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Finds the biggest the integer of a list.

    Args:
        list: my_list

    Return:
            max integer
    """

    if len(my_list) == 0:
        return None

    max_int = my_list[0]

    for int_check in my_list:
        if int_check > max_int:
            max_int = int_check

    return max_int
