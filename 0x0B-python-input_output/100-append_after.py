#!/usr/bin/python3
# 100-append_after.py
"""Defines file-txt insert func.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Args:
        filename (str): name.
        search_string (str): str to check.
        new_string (str): str to insert.
    """
    text = ""
    with open(filename) as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as file2:
        file2.write(text)
