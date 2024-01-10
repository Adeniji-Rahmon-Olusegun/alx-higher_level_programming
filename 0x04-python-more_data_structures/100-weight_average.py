#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    Computes the weighted average of all integer tuple

    Args:
        my_list: list

    Return:
          Weighted average: float
    """
    if len(my_list) == 0:
        return 0

    weights = 0
    weights_div = 0

    for tup in my_list:
        weights += (tup[0] * tup[1])
        weights_div += tup[1]

    weighted_avg = weights/weights_div

    return weighted_avg
