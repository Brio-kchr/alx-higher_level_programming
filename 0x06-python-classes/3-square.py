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
        # Private instace attribute
        if type(size) is not int:
            raise(TypeError('size must be an interger'))
        if size < 0:
            raise(ValueError('size must be >= 0'))
        self.__size = size

    def area(self):
        """
        returns the area of the square
        """
        return (self.__size) ** 2


if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)
    print("Area: {}".format(my_square.area()))

    my_square_2 = Square()
    print(type(my_square_2))
    print(my_square_2.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)
    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
    try:
        my_sq_3 = Square("3")
        print(type(my_sq_3))
        print(my_sq_3.__dict__)
    except Exception as e:
        print(e)

    try:
        my_sq_4 = Square(-89)
        print(type(my_sq_4))
        print(my_sq_4.__dict__)
    except Exception as e:
        print(e)
