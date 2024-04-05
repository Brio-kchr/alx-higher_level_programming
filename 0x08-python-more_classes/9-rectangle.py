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

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Defines the height and width of our rect
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        Prints a string repr of an object
        """
        if (self.width == 0) or (self.height == 0):
            return ""

        str_repr = ""
        for i in range(self.height):
            for i in range(self.width):
                str_repr += str(self.print_symbol)
            str_repr += "\n"
        return str_repr[:-1]

    def __repr__(self):
        """
        Prints a string repr of an object
        """
        return f'Rectangle({self.width}, {self.height})'

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

    def area(self):
        """
        To calculate area of a rectangle
        """
        return (self.width * self.height)

    def perimeter(self):
        """
        To calc perimeter of a rectangle
        """
        if (self.width == 0) or (self.height == 0):
            return 0
        else:
            return 2 * (self.width + self.height)

    def __del__(self):
        """
        To print custom message when an instance of Rect is del
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rect based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) < Rectangle.area(rect_2):
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance with width == height == size
        """
        return cls(size, size)


if __name__ == "__main__":
    my_rect = Rectangle(8, 4)
    my_rect1 = Rectangle(2, 3)
    if my_rect is Rectangle.bigger_or_equal(my_rect, my_rect1):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger or equal to my_rectangle_1")
