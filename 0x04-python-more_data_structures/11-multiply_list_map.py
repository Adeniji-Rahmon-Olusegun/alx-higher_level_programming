#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """
    Returns a list with all values multiplied by a number

    Args:
        my_list: list
        number: integer

    Return:
          list
    """
    mod_list = [ml for ml in my_list]
    return list(map(lambda arg: arg * number, mod_list))
