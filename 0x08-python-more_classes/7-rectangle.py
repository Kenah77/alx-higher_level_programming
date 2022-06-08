#!/usr/bin/python3
# 7-rectangle.py
"""Defines a Rectangle class.
"""


class Rectangle:
    """
    Attr:
        instances (int): num of rect instances.
        sign (any): used for rep str.
    """

    instances = 0
    sign = "#"

    def __init__(self, width=0, height=0):
        """
        Args:
            width (int): width
            height (int): height
        """
        type(self).instances += 1
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get/set width"""
        return self.__width

    @width.setter
    def width(self, value):
        if != int(value):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set height"""
        return self.__height

    @height.setter
    def height(self, value):
        if value != int(value):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return rep of rect"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for x in range(self.__height):
            [rectangle.append(str(self.sign)) for y in range(self.__width)]
            if x != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """Return the str rep"""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)

    def __del__(self):
        """message for deletion of Rectangle.
    """
        type(self).instances -= 1
        print("Bye rectangle...")
