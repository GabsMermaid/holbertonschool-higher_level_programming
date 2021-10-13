#!/usr/bin/python3
"""
Contains MyList class
"""


class MyList(list):
    """subclass of list"""
    def __init__(self):
        """initializes object"""
        super().__init__()

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
