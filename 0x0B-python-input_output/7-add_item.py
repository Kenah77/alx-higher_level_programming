#!/usr/bin/python3
"""add_item"""


import json
import sys
import os.path

save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"
if os.path.isfile(file):
    Myobj = load_from_json(file)
else:
    Myobj = []
Myobj.extend(sys.argv[1:])
save_to_json(Myobj, file)
