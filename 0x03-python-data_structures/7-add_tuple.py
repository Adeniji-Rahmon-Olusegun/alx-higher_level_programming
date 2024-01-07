#!/bin/usr/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two (2) tuples.

    Args:
        tuple: tuple_a
        tuple: tuple_b

    Return:
            tuple: Addition of two (2) tuples
    """

    mod_tupa = tuple_a + (0, 0)
    mod_tupb = tuple_b + (0, 0)

    return (mod_tupa[0] + mod_tupb[0], mod_tupa[0] + mod_tupb[0])
