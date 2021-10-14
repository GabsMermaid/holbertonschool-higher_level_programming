#!/usr/bin/python3
"""
Contain "save_to_json_file" function
"""

import json


def save_to_json_file(my_obj, filename):
    """writes Object to text file, using JSON representation"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
