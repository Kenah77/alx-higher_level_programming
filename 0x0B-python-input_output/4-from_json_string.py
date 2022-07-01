#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a json->object function.
"""
import json


def from_json_string(my_str):
    """Return python json
    """
    return json.loads(my_str)
