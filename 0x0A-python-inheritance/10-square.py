#!/usr/bin/python3
# 10-square.py
"""Defines a Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Repr a square."""

    def __init__(self, size):
        """instatiate.

        Args:
            size (int): size of sq.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
