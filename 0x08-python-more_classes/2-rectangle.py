#!/usr/bin/python3
# 2-rectangle.py
"""Defines Rectangle class.
"""


class Rectangle:
    """Rep a rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Args:
            width (int): width
            height (int): height
        """
        self.height = height
        self.width = width

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
        """Return the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
