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
                f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__width}"
        )
