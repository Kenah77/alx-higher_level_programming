#!/usr/bin/python3
"""student"""


class Student:
    """student"""
    def __init__(self, first_name, last_name, age):
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self):
        """to_json"""
        return self.__dict__
