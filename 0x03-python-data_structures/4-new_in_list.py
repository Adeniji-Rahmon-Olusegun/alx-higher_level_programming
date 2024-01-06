#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list without modifying
    the original list.

    Args:
        my_list: original list
        idx: index position of element to be modified
            in the new list
        element: for replacment

    Return:
            Updated copy list
            copy of my_list: if idx < -ve
            copy of my_list: if idx >= len(my_list)
    """
    copy_org_list = mylist[:]

    if (idx < 0):
        return (copy_org_list)
    elif (idx >= len(my_list)):
        return (copy_org_list)

    copy_org_list[idx] = element

    return(copy_org_list)
