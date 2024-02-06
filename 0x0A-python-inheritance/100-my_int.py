#!/usr/bin/python3
"""Module contains MyInt class"""


class MyInt(int):
    """Inverts the equality and inequality operator of int class"""

    def __eq__(self, val):
        """Overides equlaity operator"""
        return super().__ne__(val)

    def __ne__(self, val):
        """Overides inequality operator"""
        return super().__eq__(val)
