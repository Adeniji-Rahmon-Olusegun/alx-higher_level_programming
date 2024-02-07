#!/usr/bin/python3
"""Module contains Student class"""


class Student:
    """
    Defines Student attributes
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student"""

        s_json = self.__dict__

        return s_json
