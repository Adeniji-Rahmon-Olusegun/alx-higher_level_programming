#!/usr/bin/python3
""""Module contain BaseGeometry class"""


class BaseGeometry:
    """Serves as a mother/base class to other
    geometric class"""

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if value is an integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
