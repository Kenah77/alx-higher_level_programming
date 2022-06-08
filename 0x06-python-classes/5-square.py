#!/usr/bin/python3
# 5-square.py

"""Square."""


class Square:
    """Rep square."""

    def __init__(self, __size):
        """
        Args:
            __size (int): size
        """
        self.__size = __size

    @property
    def size(self):
        """Get/set size"""
        return (self.__size)

    @size.setter
    def size(self, val):
        if val != int(val):
            raise TypeError("size must be of int")
        elif val < 0:
            raise ValueError("__size must be >= 0")
        self.__size = val

    def area(self):
        """Return area"""
        return (self.__size * self.__size)

    def square(self):
        """Print square"""
        for x in range(0, self.__size):
            [print("#", end="") for y in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
