#!/usr/bin/python3
# 3-is_kind_of_class.py
"""Defines class function.
"""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance or inherited instance of a class.

    Args:
        obj : obj to lookup.
        a_class : class to compare to.
    Returns:
        If obj is instance or inherited instance of a_class - True.
        Else - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
