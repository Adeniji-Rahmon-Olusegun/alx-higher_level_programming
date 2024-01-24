#!/usr/bin/python3
"""Square class with exception"""


class Square:
    """Updated class with exception handling feature

    __init__:
        instantiate the square with a private attribute

    Attributes:
        size (int): length/breadth of a square

    Raises:
        TypeError: if size not int
        ValueError: if size < 0
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
