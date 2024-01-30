#!/usr/bin/python3
class LockedClass:
    """Prevents the user from dynamically creating
    new instances except if the new instance attribute
    is called first_name
    """
    def __setattr__(self, p_name, p_val):
        if p_name == "first_name":
            self.__dict__[p_name] = p_val
        else:
            msg = f"'LockedClass' object has no attribute '{p_name}'"
            raise AttributeError(msg)
