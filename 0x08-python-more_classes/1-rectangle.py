#!/usr/bin/python3
"""
Empty class module to define a rectangle.
"""


class Rectangle:
    """
    Class to define a rectangle

    Attrs:
        width: getter and setter for self.__width
        height: getter and setter for self.__height
        self.__height (interger): height of a rect
        self.__width (interger): width of a rect
    """
    def __init__(self, width=0, height=0):
        """
        Defines the height and width of our rect

        Args:
            height (interger): height of a rect instance
            width (interger): width of a rectangle instance
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        To retrieve rect width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        To set rect's width
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """
        To get rect's height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        To set rect's height
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height


if __name__ == "__main__":
    my_rect = Rectangle(2, 4)

    print(my_rect.__dict__)

    my_rect.width = 10
    my_rect.height = 3
    print(my_rect.__dict__)
