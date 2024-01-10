#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replaces all occurences of an element in a new list

    Args:
        my_list: list
        search: int
        replace: int

    Return:
           new_list: list
    """

    new_list = [new_me for new_me in my_list]

    for i_search in range(len(new_list)):
        if new_list[i_search] == search:
            new_list[i_search] = replace

    return new_list
