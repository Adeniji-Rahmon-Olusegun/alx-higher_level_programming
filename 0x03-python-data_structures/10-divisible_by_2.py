#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in a list

    Args:
        list: my_list

    Return:
            list: containing boolean (True or False)
    """

    if my_list:

        check_div_2 = []

        for happy_2_checker in myList:
            if happy_2_checker % 2 == 0:
                check_div_2 += list(True)
            else:
                check_div_2 += list(False)

        return check_div_2
