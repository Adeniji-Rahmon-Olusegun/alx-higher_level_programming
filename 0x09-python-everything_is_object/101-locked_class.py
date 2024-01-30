#!/usr/bin/python3

class LockedClass:
    """Prevents the user from dynamically creating
    new instances except if the new instance attribute
    is called first_name
    """

    __slots__ = ("first_name",)
