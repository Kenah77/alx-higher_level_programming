#!/usr/bin/python3
# 7-save_to_json_file.py
"""Defines json file-writing func.
"""
import json


def save_to_json_file(my_obj, filename):
    """Write object to txt file using json rep.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
