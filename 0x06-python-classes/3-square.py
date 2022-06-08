#!/usr/bin/python3
# 3-square.py

"""Square."""


class Square:
    """Rep square."""

    def __init__(self, __size=0):
        """
        Args:
            __size (int): size
        """
        if __size != int(__size):
            raise TypeError("__size must be of integer")
        elif __size < 0:
            raise ValueError("__size must be >= 0")
        self.__size = __size

    def area(self):
        """Return area"""
        return (self.__size * self.__size)

