#!/usr/bin/python3

def no_c(my_string):
    """
    Removes all character c and C from a string

    Args:
        my_string

    Return:
            new_string
    """
    if my_string:

        new_string = ""

        for char_check in my_string:
            if char_check != 'c' and char_check != 'C':
                new_string += char_check

        return (new_string)
    return (my_string)
