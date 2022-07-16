#!/usr/bin/python3
""" defines test for the triangle class"""


import os
from unittest import TestCase
from models.base import Base
from models.rectangle import Rectangle


class TriangleTestCases(TestCase):
    """ the test cases for the triangle classes as a method """

    def test_instance_of_base(self):
        """ test if instances are instance of Base and Rectangle"""
        self.assertIsInstance(Rectangle(2, 3), Base)

    def test_instance_of_rectangle(self):
        self.assertIsInstance(Rectangle(2, 3), Rectangle)

    def test_width_rigth(self):
        t = Rectangle(2, 3)
        self.assertEqual(t.width, 2)

    def test_height_right(self):
        t = Rectangle(2, 3)
        self.assertEqual(t.height, 3)

    def test_id_multiple_none(self):
        r = Rectangle(4, 3, 4, 5)
        i = Rectangle(2, 1, 3, 5)
        self.assertEqual(i.id, r.id + 1)


    def test_width_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(2.5, 2)

    def test_width_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(-2, 1)

    def test_height_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 2.5)

    def test_width_type_error(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_x_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 2.5)

    def test_x_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -2)

    def test_y_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 1, -2.5)
    def test_y_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 1, -2)

    def test_area(self):
        t = Rectangle(1, 4)
        self.assertEqual(t.area(), 4)


"""if __name__ == 'main':
    unittest.main()
"""
