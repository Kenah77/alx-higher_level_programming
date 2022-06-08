#!/usr/bin/python3
"""print_square
"""


def print_square(size):
    """Prints square
    """
    if type(size) != int:
        raise TypeError("size must be of int")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
