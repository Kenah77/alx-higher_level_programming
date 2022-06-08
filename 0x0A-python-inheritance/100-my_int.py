#!/usr/bin/python3
# 100-my_int.py
"""Defines a class MyInt which inherits int.
"""


class MyInt(int):

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
