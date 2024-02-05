#!/usr/bin/python3
"""MyList inherits list"""


class MyList(list):
    """This inherits properties of list"""

    def print_sorted(self):
        """Sorts a list"""

        print(sorted(list((self))))
