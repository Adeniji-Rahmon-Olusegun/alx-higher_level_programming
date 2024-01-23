#!/usr/bin/python3

def safe_function(fct, *args):
    """
    Executes a function safely

    Args:
        fct: function
        *args: variable length argument

    Return:
            Result of the function execution and None otherwise
    """
    import sys

    try:
        funct_res = fct(*args)
        return funct_res
    except Exception as funte:
        sys.stderr.write("Exception: {}\n".format(funte))
        return None
