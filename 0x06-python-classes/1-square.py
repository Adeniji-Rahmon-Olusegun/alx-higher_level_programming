#!/usr/bin/python3
"""Square class with square attribute"""


class Square:
    """Has the size of sqaure as private instance attribute

    __init__ clares the size attribute as private instance attribute

    Atributes:
        size (init): size of the square
    """
    def __init__(self, size):
        self.__size = size
