#!/usr/bin/python3
""" define the test cases for a max_integer function """

from unittest import TestCase
max_int = __import__('6-max_integer').max_integer


class TestMaxInteger(TestCase):
    """the unit class for max_int"""

    def test_result(self):
        """ test for good path correct output"""

        self.assertEqual(max_int([2, 7]), 7)
        self.assertEqual(max_int(), None)
        self.assertEqual(max_int([-3, -7]), -3)
        self.assertEqual(max_int([1, 3, -2]), 3)

        """def test_type(self):
         #test for bad path raise type error

         self.assertRaises(TypeError, max_int, "string")
         self.assertRaises(TypeError, max_int, False)
         self.assertRaises(TypeError, max_int, (2, 3))"""
