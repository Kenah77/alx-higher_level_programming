#!/usr/bin/python3
# 9-rectangle.py
"""Defines class Rectangle that inherit BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rep a rectangle."""

    def __init__(self, width, height):
        """instatiate.

        Args:
            width (int): width
            height (int): height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return area
    """
        return self.__width * self.__height

    def __str__(self):
        st = "[" + str(self.__class__.__name__) + "] "
        st += str(self.__width) + "/" + str(self.__height)
        return st
