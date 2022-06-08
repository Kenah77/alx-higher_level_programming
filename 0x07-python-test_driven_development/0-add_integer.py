#!/usr/bin/python3
"""Defines func that adds two number
"""


def add_integer(a, b=98):
    """Adds two nums
    """
    if a != int(a) and a != float(a):
        raise TypeError("a must be int")
    if b != int(b) and b != int(b):
        raise TypeError("b must be int")
    return a + b
