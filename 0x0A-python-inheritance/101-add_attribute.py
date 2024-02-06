#!/usr/bin/python3
"""Module contains add_attribute function"""


def add_attribute(objects, obj_name, obj_value):
    """
    Adds a new attribute to an object

    Args:
        objects: object to which the attribute is added
        obj_name: attribute name
        obj_value: value of attribute to be added

    Raises:
        TypeError: if new attribute cannot be added
    """
    if hasattr(objects, '__dict__') or hasattr(type(objects), '__dict__'):
        setattr(objects, obj_name, obj_value)
    raise TypeError("can't add new attribute")
