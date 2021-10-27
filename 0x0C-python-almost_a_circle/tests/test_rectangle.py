#!/usr/bin/python3
"""
Test file for Rectangle class
"""

import unittest
from tests import *
from models.Base import Base
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """
    Test needed for Rectangle class
    1.rectangle with 2,3 & 4 arguments
    2.rectangle with 2,3 & 4 args and one being a str
    3.
    4.
    5.
    6.
    7.
    8.
    9.
    """

    @classmethod
    def setUpClass(self):
        self.a_rectangle = Rectangle(1, 2)
        self.b_rectangle = Rectangle(1, 2, 3)
        self.c_rectangle = Rectangle(1, 2, 3, 4)
        self.d_rectangle = Rectangle(1, 2, 3, 4, 5)

    def test_init(self):
        self.assertEqual(self.a_rectangle.id, 1)
