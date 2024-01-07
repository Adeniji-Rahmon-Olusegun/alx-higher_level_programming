#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Deletes item at a specific index position

    Args:
        list: my_list
        int: idx (index postion)

    Return:
            list: modified list
    """
    if my_list:

        if idx < 0 or idx >= len(my_list):
            return my_list

        new_list_after_deletion = my_list[:idx] + my_list[(idx + 1):]

        return new_list_after_deletion
