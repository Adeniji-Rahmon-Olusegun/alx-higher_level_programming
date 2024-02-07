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

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student"""

        stud_info =  {"first_name": self.first_name, "last_name": self.last_name,
                "age": self.age}

        cond_1 = isinstance(attrs, list)

        if attrs is not None:
            cond_2 =  all(isinstance(element, str) for element in attrs)
        bool_state = cond_1 and cond_2

        if bool_state:
            stud_info = {k: v for k, v in stud_info.items() if k in attrs}
        return stud_info
