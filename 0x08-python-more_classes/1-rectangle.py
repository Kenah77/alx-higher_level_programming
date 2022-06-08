#!/usr/bin/python3
# 1-rectangle.py
"""Defines Rectangle class.
"""


class Rectangle:
    """Rep rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Args:
            width (int): width
            height (int): heigh
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get/set the width"""
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
        """Get/set the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if value != int(value):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
