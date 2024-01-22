#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list

    Args:
        my_list: list
        x: int

    Return:
          num of items printed: int
    """
    item_count = 0

    try:
        for item in range(x):
            print("{}".format(my_list[item]), end="")
            item_count += 1
    except IndexError:
        pass

    print()

    return item_count
