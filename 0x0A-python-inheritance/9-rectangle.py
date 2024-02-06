#!/usr/bin/python3
"""This module contains class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class inherits BaseGeometry properties"""

    def __str__(self):
        return f"[Rectangle] <width>/<height>"

    def __repr__(self):
        return f"[Rectangle] <width>/<height>"

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Computes the area of a the Rectangle"""
        return self.__width * self.__height
