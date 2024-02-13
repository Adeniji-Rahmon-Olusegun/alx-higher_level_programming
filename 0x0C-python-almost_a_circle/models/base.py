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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Json representation of list_dictionary"""

        if not list_dictionaries:
            return "[]"
        dump = json.dumps(list_dictionaries)

        return dump

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of list_objs to a file"""

        if list_objs is None:
            list_objs = []
        else:
            list_objs = [obj_cls.to_dictionary() for obj_cls in list_objs]

        filename = f"{cls.__name__}.json"

        dump_obj = cls.to_json_string(list_objs)

        with open(filename, "w") as file_obj:
            file_obj.write(dump_obj)

    @staticmethod
    def from_json_string(json_string):
        """Returns list of the JSON string representation json_string"""

        if not json_string:
            return []
        return json.loads(json_string)
