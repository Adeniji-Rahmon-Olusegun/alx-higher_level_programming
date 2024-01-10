#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square of all integers of a matrix

    Args:
        matrix: List of list

    Return:
            Matrix containing the square of values in the
            original matrix
    """
    squared_matrix = matrix.copy()

    dic_m = {"dmatrix": squared_matrix}

    for matl in range(len(dic_m["dmatrix"])):
        for idx in range(len(dic_m["dmatrix"][matl])):
            dic_m["dmatrix"][matl][idx] = (dic_m["dmatrix"][matl][idx])**2

    return (dic_m["dmatrix"])
