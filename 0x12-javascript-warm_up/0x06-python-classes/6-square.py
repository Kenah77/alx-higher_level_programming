#!/usr/bin/python3
# 6-square.py
"""Square."""


class Square:
    """Rep square"""

    def __init__(self, size=0, position=(0, 0)):
        """
            Args:
            size (int): size
            position (int, int): position

        """
        self.position = position
        self.size = size

    @property
    def size(self):
        """Get/set size"""
        return (self.__size)

    @size.setter
    def size(self, val):
        if val != int(val):
            raise TypeError("size must be of integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val

    @property
    def position(self):
        """Get/set current position"""
        return (self.__position)

    @position.setter
    def pos(self, val):
        if val != tuple(val) or
                len(val) != 2 or
                not all(isinstance(num, int) for num in val) or
                not all(num >= 0 for num in val)):
            raise TypeError("position must be a tuple of 2 positive int")
        self.__position = val

    def area(self):
        """Return area"""
        return (self.__size * self.__size)

    def square(self):
        """Print square"""
        if self.__size == 0:
            print("")
            return

        [print("") for x in range(0, self.__position[1])]
        for x in range(0, self.__size):
            [print(" ", end="") for y in range(0, self.__position[0])]
            [print("#", end="") for i in range(0, self.__size)]
            print("")
