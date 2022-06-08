#!/usr/bin/python3
# 11-square.py
"""Defines Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rep square."""

    def __init__(self, size):
        """instatiate

        Args:
            size (int): size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
