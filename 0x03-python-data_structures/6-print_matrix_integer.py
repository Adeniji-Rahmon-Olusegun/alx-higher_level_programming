#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers

    Args:
        matrix

    Return:
            None
    """
    for first_list in range(len(matrix)):
        for second_list in range(len(matrix[0])):
            print("{:d}".format(matrix[first_list][second_list]), end=" ")
        print(end='\n')
