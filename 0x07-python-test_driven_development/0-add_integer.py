#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: first number (int or float)
        b: second number (int or float)

    Return:
        sum of two integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
