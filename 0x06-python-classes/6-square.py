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

    def __init__(self, size=0, position=(0, 0):
        """
        Method to initialize and set square size

        Args:
            size: sides of a square legth
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Returns position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets position value
        """
        if (type(value) is not tuple) or (len(position) != 2) or\
                (type(position[0] != int)) or (position[0] < 0) or\
                (type(position[1] != int)) or (position[1] < 0):
            raise(TypeError('position must be a tuple of 2 positive integers'))
        self.__position = position
        

    def area(self):
        """
        Returns area of the square
        """
        return (self.__size) ** 2

    def my_print(self):
        """
        Prints in stdout the square with character #
        """
        if self.__size == 0:
            print("")
        else:
            for y in range(0, self.__position[1]):
                print("")
            for i in range(0, self.__size):
                for x in range(0, self.position[0]):
                    print(" ",end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print("")


if __name__ == "__main__":
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    print("--")
    my_square.my_print()
    print("--")
    my_square.size = 0
    my_square.my_print()
    print("---")
    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
