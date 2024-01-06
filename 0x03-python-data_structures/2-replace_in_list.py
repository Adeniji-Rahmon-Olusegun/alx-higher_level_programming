#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replaces en element of a list with another

    Args:
        my_list: list of elemets
        idx: index position of element to be replaced
        element: for replacement

    Return:
            Update list
            my_list: if idx is -ve
            my_list: if idx >= len(my_list)
    """
    if (idx < 0):
        return (my_list)
    elif (idx >= len(my_list)):
        return (my_list)

    my_list[idx] = element
    return (my_list)
