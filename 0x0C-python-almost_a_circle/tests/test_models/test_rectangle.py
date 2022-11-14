#!/usr/bin/python3
""" defines test for the rectangle class"""


import io
import sys
from unittest import TestCase
from models.base import Base
from models.rectangle import Rectangle


class TriangleTestCases(TestCase):
    """ the test cases for the rectangle class """

    def test_instance_of_base(self):
        """ test if instances are instance of Base and Rectangle"""
        self.assertIsInstance(Rectangle(2, 3), Base)

    def test_instance_of_rectangle(self):
        """ test if instance is an instance of rectange or base"""
        self.assertIsInstance(Rectangle(2, 3), Rectangle)

    def test_width_rigth(self):
        """ test if width is correct """
        t = Rectangle(2, 3)
        self.assertEqual(t.width, 2)

    def test_height_right(self):
        """ test if height is correct"""
        t = Rectangle(2, 3)
        self.assertEqual(t.height, 3)

    def test_id_multiple_none(self):
        """ test if id is set automatically"""
        r = Rectangle(4, 3, 4, 5)
        i = Rectangle(2, 1, 3, 5)
        self.assertEqual(i.id, r.id + 1)

    def test_width_type_error(self):
        """test to see if type error is raised"""
        with self.assertRaises(TypeError):
            Rectangle(2.5, 2)

    def test_width_type_error2(self):
        """test setting by . dot """
        with self.assertRaises(TypeError):
            r = Rectangle(3, 4)
            r.width = "3"
        with self.assertRaises(TypeError):
            Rectangle("3", 1)

    def test_width_value_error(self):
        """test to see if ValueError is raised"""
        with self.assertRaises(ValueError):
            Rectangle(-2, 1)

    def test_height_type_error(self):
        """test to see if typeError is raised"""
        with self.assertRaises(TypeError):
            Rectangle(2, 2.5)
        with self.assertRaises(TypeError):
            Rectangle(2, "3")

    def test_height_value_error(self):
        """test to see if valueError is raised"""
        with self.assertRaises(ValueError):
            Rectangle(2, 0)

    def test_width_type_error(self):
        """test to see if valueError is raised wrong width"""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_x_type_error(self):
        """test for type error"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 2.5)

    def test_x_value_error(self):
        """test for x value error"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -2)

    def test_y_type_error(self):
        """test for correct y type"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 1, -2.5)

    def test_y_value_error(self):
        """test for correct y value"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 1, -2)

    def test_area(self):
        """test to see if area is correct"""
        t = Rectangle(1, 4)
        self.assertEqual(t.area(), 4)

    def test_display_with_hash(self):
        """test to see if display print expected output"""
        t = Rectangle(2, 3)
        capture_output = io.StringIO()
        sys.stdout = capture_output
        t.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capture_output.getvalue(), "##\n##\n##\n")

    def test_display_with_axis(self):
        """test display of rectangle with axis"""
        r = Rectangle(2, 3, 2, 2)
        capture_output = io.StringIO()
        sys.stdout = capture_output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capture_output.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_string(self):
        """test if the string representation is right"""
        t = Rectangle(1, 4, 3, 2, 12)
        self.assertEqual(str(t), "[Rectangle] (12) 3/2 - 1/4")

    def test_string_x_zero(self):
        """test if the string representation is rigth y=0"""
        r = Rectangle(2, 3, 0, 2)
        capture_output = io.StringIO()
        sys.stdout = capture_output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capture_output.getvalue(), "\n\n##\n##\n##\n")

    def test_string_y_zero(self):
        """test if the string representation is rigth y=0"""
        r = Rectangle(2, 3, 2, 0)
        capture_output = io.StringIO()
        sys.stdout = capture_output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capture_output.getvalue(), "  ##\n  ##\n  ##\n")

    def test_update(self):
        """test for all update"""
        r = Rectangle(2, 3, 2, 0)
        r.update(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (1) 4/5 - 2/3")

    def test_update_id(self):
        """test for id update"""
        r = Rectangle(2, 3, 2, 0, 10)
        r.update(1)
        self.assertEqual(str(r), "[Rectangle] (1) 2/0 - 2/3")

    def test_update_idnwidth(self):
        """test for id and width update"""
        r = Rectangle(2, 3, 2, 0, 10)
        r.update(1, 5)
        self.assertEqual(str(r), "[Rectangle] (1) 2/0 - 5/3")

    def test_update_len3(self):
        """test for id, width, height update"""
        r = Rectangle(2, 3, 2, 0, 10)
        r.update(1, 5, 7)
        self.assertEqual(str(r), "[Rectangle] (1) 2/0 - 5/7")

    def test_updatelen4(self):
        """tesst id, width, height, x update"""
        r = Rectangle(2, 3, 2, 0, 10)
        r.update(1, 5, 7, 9)
        self.assertEqual(str(r), "[Rectangle] (1) 9/0 - 5/7")

    def test_updatedict1(self):
        """test for 1 items"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/1")

    def test_updatedictid(self):
        """test for updte of 1 items"""
        r = Rectangle(10, 10, 10, 10)
        r.update(id=2)
        self.assertEqual(str(r), "[Rectangle] (2) 10/10 - 10/10")

    def test_updatedict2(self):
        """test for update of 2 items"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=3, height=4)
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 3/4")

    def test_updatedict3(self):
        """test for update of 3 items"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=3, height=4, x=2)
        self.assertEqual(str(r), "[Rectangle] (10) 2/10 - 3/4")

    def test_updatedict4(self):
        """test for update of 4 items"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=3, height=4, x=2, y=3)
        self.assertEqual(str(r), "[Rectangle] (10) 2/3 - 3/4")

    def test_updatedict5(self):
        """The test for update of five items"""
        r = Rectangle(10, 10, 10, 10)
        r.update(width=3, height=4, x=2, y=3, id=1)
        self.assertEqual(str(r), "[Rectangle] (1) 2/3 - 3/4")

    def test_to_dict(self):
        """test the to_dictionary method"""
        r = Rectangle(10, 10, 10, 10, 10)
        self.assertDictEqual(r.to_dictionary(), {
            "id": 10, "width": 10, "height": 10, "x": 10, "y": 10
        })
