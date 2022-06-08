#!/usr/bin/python3
# 101-add_attribute.py
"""Define func that adds attr
"""


def add_attribute(obj, att, value):
    """
    Args:
        obj : obj to add attr
        att : name of attr.
        value : value.
    Raises:
        TypeError: If attribute can't add.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
