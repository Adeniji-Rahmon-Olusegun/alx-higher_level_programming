#!/usr/bin/python3
# module contains peak function

def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers
    """
    low_bound, upper_bound = 0, len(list_of_integers) - 1

    while low_bound <= upper_bound:
        mid_point = (low_bound + upper_bound) // 2

        if list_of_integers[mid_point] < list_of_integers[mid_point + 1]:
            low_bound = mid_point + 1
        else:
            upper_bound = mid_point - 1
    return list_of_integers[low_bound]

