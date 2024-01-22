#!/usr/bin/python3

def safe_print_integer(value):
    """
    Prints an integer

    Args:
        value: (str, int, etc.,)

    Return:
          bool
    """

    try:
        real_val = int(value)
        print("{:d}".format(real_val))
        return True
    except ValueError:
        return False
