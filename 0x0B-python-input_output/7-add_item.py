#!/usr/bin/python3
"""Module contains functions that load, add and save data"""

import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

user_args = sys.argv[1:]


try:
    user_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    user_list = []

user_list.extend(user_args)

save_to_json_file(user_list, "add_item.json")
