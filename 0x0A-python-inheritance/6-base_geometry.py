#!/usr/bin/python3
""""Module contain BaseGeometry class"""


class BaseGeometry:
    """Serves as a mother/base class to other
    geometric class"""

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")
