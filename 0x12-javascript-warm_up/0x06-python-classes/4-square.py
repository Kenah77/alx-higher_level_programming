#!/usr/bin/python3
# 4-square.py
"""Square."""


class Square:
    """Rep square."""

    def __init__(self, __size=0):
        """
        Args:
            __size (int): __size
        """
        self.__size = __size

    @property
    def size(self):
        """Get/set __size"""
        return (self.__size)

    @size.setter
    def size(self, val):
        if val != int(val):
            raise TypeError("size must be of integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area"""
        return (self.__size * self.__size)
