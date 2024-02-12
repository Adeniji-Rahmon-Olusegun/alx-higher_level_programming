#!/usr/bin/python3
"""Module contains Base class"""


class Base:
    """Parent class to other geometry class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
