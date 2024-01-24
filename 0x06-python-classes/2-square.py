#!/usr/bin/python3
"""Square class with exception"""


class Square:
    """Updated class with exception handling feature

    __init__:
        instantiate the square with a private attribute

    Attributes:
        size (int): length/breadth of a square
    """
    def __init__(self, size=0):
        try:
            if not isinstance(size, int):
                raise TypeError
            elif size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
        else:
            self.__size = size
