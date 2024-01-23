#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list and only
    integers

    Args:
        my_list: list
        x: number of elements to be printed (int)

    Return:
            number of elements successfully printed
    """
    try:
        item_count = 0

        for item in range(x):
            if isinstance(my_list[item], int):
                print("{:d}".format(my_list[item]), end="")
                item_count += 1
    except (ValueError, TypeError):
        pass
    print()

    return item_count
