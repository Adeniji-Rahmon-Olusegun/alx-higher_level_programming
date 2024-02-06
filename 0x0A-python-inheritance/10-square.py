#!/usr/bin/python3
"""Module contains Square class"""

BaseGeometry = __import__('6-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square inherits from Rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Computes the area of a Square"""
        return self.__size * self.__size
