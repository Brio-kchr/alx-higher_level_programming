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

    def __init__(self, size=None):
        """
        Method to initialize and set square size

        Args:
            size: sides of a square legth
        """
        # Private instace attribute
        self.__size = size


if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)
    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
