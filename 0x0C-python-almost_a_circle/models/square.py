#!/usr/bin/python3
"""
Module creates class Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """representation of square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize square"""
        super().__init__(size, size, x, y, id)
        self.size = size
