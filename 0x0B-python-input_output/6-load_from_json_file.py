#!/usr/bin/python3
# 8-load_from_json_file.py
"""Defines json file-read func.
"""
import json


def load_from_json_file(filename):
    """Create python obj from a json file.
    """
    with open(filename) as file:
        return json.load(file)
