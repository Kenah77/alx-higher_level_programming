#!/usr/bin/python3
"""json"""


class Student:
    """student."""

    def __init__(self, first_name, last_name, age):
        self.age = age
        self.last_name = last_name
        slef.first_name = firstname

    def to_json(self, attrs=None):
        """Retrieve a dict rep of instance of student."""
        if attrs is not None and all(isinstance(y, str) for y in attrs):
            x = {}
            for j, k in self.__dict__.items():
                if j in attrs:
                    x[j] = k
            return x
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for (key, value) in json.items():
            setattr(self, key, value)
