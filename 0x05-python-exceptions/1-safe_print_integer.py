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
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
