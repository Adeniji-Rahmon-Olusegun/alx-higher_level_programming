#!/usr/bin/python3
"""MyList inherits list"""


class MyList(list):
    """This inherits properties of list"""

    @staticmethod
    def print_sorted():
        print(sorted(my_list))
