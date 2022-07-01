#!/usr/bin/python3
# 0-read_file.py


def read_file(filename=""):
    """Print the contents of a UTF8 txt file to standard output.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
