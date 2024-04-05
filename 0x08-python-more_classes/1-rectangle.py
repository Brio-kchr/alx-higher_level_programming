#!/usr/bin/python3
"""
Empty class module to define a rectangle.
"""


class Rectangle:
    """
    Class to define a rectangle

    Attrs:
        width - width of rect
            -Must be int., > 0
        height - height of the rect
            -Must be int., > 0
    """
    def __init__(self, width=0, height=0):
        """
        Defines the height and width of our rect
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        To retrieve rect width
        """
        return self.width

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
        return self.height

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
