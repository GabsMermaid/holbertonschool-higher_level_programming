#!/usr/bin/python3
"""
Contains class BaseGeometry
"""


class BaseGeometry:
    """Class with public attribute area"""
    def area(self):
        """Raises exception when called"""
        raise Exception("area() is not implemented")
