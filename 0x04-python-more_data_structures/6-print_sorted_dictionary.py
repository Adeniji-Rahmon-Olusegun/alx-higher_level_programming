#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys

    Args:
        a_dictionary: dictionary

    Return:
          None
    """
    i_am_the_sorted_dict = dict(sorted(a_dictionary.items()))

    for K, V in i_am_the_sorted_dict.items():
        print("{}: {}".format(K, V))
