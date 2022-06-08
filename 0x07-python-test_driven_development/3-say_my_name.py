#!/usr/bin/python3
"""Defines func which print full name
"""


def say_my_name(first_name, last_name=""):
    """Prints str
    """
    if type(first_name) != str:
        raise TypeError("first_name must be of str")
    if type(last_name) != str:
        raise TypeError("last_name must be of str")
    print("My name is {} {}".format(first_name, last_name))
