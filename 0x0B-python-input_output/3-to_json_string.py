#!/usr/bin/python3
# 5-to_json_string.py
"""Defines string->json function.
"""
import json


def to_json_string(my_obj):
    """Return the json
    """
    return json.dumps(my_obj)
