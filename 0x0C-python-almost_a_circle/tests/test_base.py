#!/usr/bin/python3

"""
Test file for Base class
"""

import unittest
from tests import *
from models.base import Base


class Test_Base(unittest.TestCase):
    """
    Tests needed for Base class:
    1.assigning aut an ID exists*
    2.assignin aut and ID +1*
    3.assigning ID bassed on assign argument*
    4.JSON string passing None*
    5.JSON string passing []*
    6.JSON string passing [] with {}*
    7.JSON string passing [] with {} return exist*
    8.from JSON (same as 4, 5, 6 & 7)
    """

    @classmethod
    def setUpClass(self):
        self.a_base = Base()
        self.b_base = Base()
        self.c_base = Base(89)

    def test_init(self):
        self.assertEqual(self.a_base.id, 1)
        self.assertEqual(self.b_base.id, 2)

    def test_assignID(self):
        self.assertEqual(self.c_base.id, 89)

    def test_to_JSON_str(self):
        self.assertEqual(self.a_base.to_json_string(None), '[]')
        self.assertEqual(self.a_base.to_json_string([]), '[]')
        self.assertTrue(type(self.a_base.to_json_string([{ 'id': 12 }])), str)

    def test_from_JSON_str(self):
        self.assertEqual(self.a_base.from_json_string(None), [])
        self.assertEqual(self.a_base.from_json_string([]), [])
        self.assertTrue(type(self.a_base.to_json_string([{ "id": 89 }])), str)

