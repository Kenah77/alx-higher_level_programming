#!/usr/bin/python3
# 4-inherits_from.py
"""Defines inherited class-check func.
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj : obj to check.
        a_class (type): the referrence.
    Returns:
        If obj is an inherited instance of a_class - True.
        Else - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
