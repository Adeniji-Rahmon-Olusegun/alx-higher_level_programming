#!/usr/bin/python3
"""Square class with exception"""


class Square:
    """Updated class with exception handling feature

    __init__:
        instantiate the square with a private attribute

    Attributes:
        size (int): length/breadth of a square
        position (int): coordinates of sqaure

    Raises:
        TypeError: if size not int
        ValueError: if size < 0
    """
    def __init__(self, size=0, position=(0, 0)):

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieves the value of size

        Return:
            size (int)
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve coordinates of the square

        Return:
            position (tuple)
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the values of postion"""
        err_msg = "position must be a tuple of 2 positive integers"
        if type(value) != tuple or len(value) != 2:
            raise TypeError(err_msg)
        if any(type(i) != int for i in value) or any(j < 0 for j in value):
            raise TypeError(err_msg)
        self.__position = value

    def area(self):
        """Computes the area of a square

        Args:
            None

        Returns:
            Area (int): Area of a square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Prints a suare using # symbol"""
        if self.__size == 0:
            print()
        else:
            for y_cord in range(self.__position[1]):
                print()
            for s in range(self.__size):
                for x_cord in range(self.__position[0]):
                    print(" ", end="")
                for si in range(self.__size):
                    print("#", end="")
                print()
