#!/usr/bin/python3
# 8-rectangle.py
"""Defines Rectangle class."""


class Rectangle:
    """Rep rectangle.

    Attr:
        instances (int): num of rect instances.
        sign (any): used for str rep.
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
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set width"""
        return self.__width

    @width.setter
    def width(self, value):
        if value != int(value):
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
        elif value < 0:
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

    @staticmethod
    def bigger_or_equal(rectangle1, rectangle2):
        if not isinstance(rectangle1, Rectangle):
            raise TypeError("rectangle1 must be an instance of Rectangle")
        if not isinstance(rectangle2, Rectangle):
            raise TypeError("rectangle2 must be an instance of Rectangle")
        if rectangle1.area() >= rectangle2.area():
            return (rectangle1)
        return (rectangle2)

    def __str__(self):
        """Return rep rect"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for x in range(self.__height):
            [rectangle.append(str(self.sign)) for y in range(self.__width)]
            if x != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """Return str rep"""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)

    def __del__(self):
        """message for deletion of Rectangle.
    """
        type(self).instances -= 1
        print("Bye rectangle...")
