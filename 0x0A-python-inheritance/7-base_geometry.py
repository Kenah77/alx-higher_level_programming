#!/usr/bin/python3
# 7-base_geometry.py
"""Defines class BaseGeometry.
"""


class BaseGeometry:
    """Rep base geometry.
    """

    def area(self):
        """nothing.
    """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check whether param is int.

        Args:
            name (str): name f param.
            value (int): param to check.
        Raises:
            TypeError: If value not int.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
