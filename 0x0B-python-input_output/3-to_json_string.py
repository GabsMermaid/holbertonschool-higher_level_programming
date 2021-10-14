#!/usr/bin/python3
"""
Contain "to_json_string" function
"""

import json


def to_json_string(my_obj):
    """return JSON representation of object"""
    return json.dumps(my_obj)
