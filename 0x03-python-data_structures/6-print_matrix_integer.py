#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers

    Args:
        matrix

    Return:
            None
    """
    if not matrix:
        return

    lt = len(matrix[0]) - 1

    for fl in matrix:
        for sdl in range(len(fl)):
            print("{:d}".format(fl[sdl]), end=" " if sdl != lt else "")
        print(end='\n')
