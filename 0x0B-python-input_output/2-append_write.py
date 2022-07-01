#!/usr/bin/python3
# 4-append_write.py
"""Defines a file-append function.
"""


def append_write(filename="", text=""):
    """
    Args:
        filename: name of the file to append to.
        text: str to append to the file.
    Returns:
        num of chars appended.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
