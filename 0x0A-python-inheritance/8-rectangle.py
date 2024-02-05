#!/usr/bin/python3
"""This module contains class Rectangle"""


class Rectangle(BaseGeometry):
    """This class inherits BaseGeometry properties"""

    def __init__(self, width, heigth):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("heigth", heigth)
        self.__heigth = heigth
