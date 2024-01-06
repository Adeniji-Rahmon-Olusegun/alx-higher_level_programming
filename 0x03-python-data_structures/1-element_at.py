#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Retrieves an element from a list

    Args:
        my_list: list of objects/elemets
        idx: index position of a random element

    Return:
            None: if idx -ve
            None: if idx > len my_list
            Element at idx position
    """

    if (idx < 0):
        return (None)
    elif (idx >= len(my_list)):
        return (None)
    return (my_list[idx])
