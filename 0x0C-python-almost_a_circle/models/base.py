#!/usr/bin/python3
"""Module contains Base class"""

import json


class Base:
    """Parent class to other geometry class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Json representation of list_dictionary"""

        if list_dictionaries is None:
            return "[]"        
        dump =  json.dumps(list_dictionaries)

        return dump
