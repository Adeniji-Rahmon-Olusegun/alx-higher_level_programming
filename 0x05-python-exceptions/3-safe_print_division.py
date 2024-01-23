#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Divides 2 integers and print the result

    Args:
        a: first number (int)
        b: second number (int)

    Return:
            result of division or None otherwise
    """
    try:
        result_div = a/b
        return result_div
    except ZeroDivisionError:
        result_div = None
        return result_div
    finally:
        print("Inside result: {}".format(result_div))
