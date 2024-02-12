#!/usr/bin/python3
"""Module contains Square class"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Sqaure inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return (
                f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
        )

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns argumet to public attributes"""

        if args:
            attr = ["id", "size", "x", "y"]

            for idx, param in enumerate(args):
                setattr(self, attr[idx], param)
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)
