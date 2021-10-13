#!/usr/bin/python3
"""
Contains function is_same_class
"""


def is_same_class(obj, a_class):
    """return True if obj is exact class a_class, otherwise False"""
    return (type(obj) == a_class)
