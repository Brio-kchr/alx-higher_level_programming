#!/usr/bin/python3
"""
Class module to define a square
Instantiated with size (no type/value verification)
"""


class Square:
    """
    Class that defines a square
    With a private instance attr size

    Attrs:
        self.__size: side length of a square instance
    """

    def __init__(self, size=0):
        """
        Method to initialize and set square size

        Args:
            size: sides of a square legth
        """
        self.__size = size

    @property
    def size(self):
        """
        getter - gets the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter - sets the size of the square
        """
        if type(value) is not int:
            raise(TypeError('size must be an interger'))
        if value < 0:
            raise(ValueError('size must be >= 0'))
        self.__size = value

    def area(self):
        """
        Returns area of the square
        """
        return (self.__size) ** 2


if __name__ == "__main__":
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
