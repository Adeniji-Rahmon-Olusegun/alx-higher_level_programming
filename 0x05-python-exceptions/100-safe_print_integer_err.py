#!/usr/bin/python3

def safe_print_integer_err(value):
    """
    Prints an integer

    Args:
        value: (str, int, float, etc.)

    Return:
            bool: True if value is integer and False otherwise
    """
    import sys

    try:
        print("{:d}".format(value))
        return True
    except Exception as vte:
        sys.stderr.write("Exception: {}\n".format(vte))
        return False
