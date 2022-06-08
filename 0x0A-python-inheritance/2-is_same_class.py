#!/usr/bin/python3
# 2-is_same_class.py
"""Defines func-check class.
"""


def is_same_class(obj, a_class):
    """Check if obj is an instance of a given class.

    Args:
        obj (any): obj to lookup.
        a_class (type): class to compare.
    Returns:
        If instance of a class - True.
        Else - False.
    """
    if type(obj) == a_class:
        return True
    return False
