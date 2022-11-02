#!/usr/bin/python3
""" defines test for the triangle class"""


import io
import sys
from unittest import TestCase
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class SquareTestCases(TestCase):
    """ the test cases for the triangle classes as a method """

    def test_instance_of_base(self):
        """ test if instances are instance of Base"""
        self.assertIsInstance(Square(3), Base)

    def test_instance_of_rectangle(self):
        """ test if instance is an instance of Rectangle"""
        self.assertIsInstance(Square(3), Rectangle)

    def test_instance_of_square(self):
        """test if square is an instance of square"""
        self.assertIsInstance(Square(3), Square)

    def test_width_rigth(self):
        """ test if width is correct """
        s = Square(3)
        self.assertEqual(s.height, 3)

    def test_height_right(self):
        """ test if height is correct"""
        s = Square(3)
        self.assertEqual(s.height, 3)

    def test_heightequalwidth(self):
        """test if height and width are same"""
        s = Square(3)
        self.assertEqual(s.height, s.width)    

    def test_id_multiple_none(self):
        """ test if id is set automatically"""
        r = Square(3)
        i = Square(2)
        self.assertEqual(i.id, r.id + 1)

    def test_width_type_error(self):
        """test to see if type error is raised"""
        with self.assertRaises(TypeError):
            Square(2.5)

    def test_width_value_error(self):
        """test to see if ValueError is raised"""
        with self.assertRaises(ValueError):
            Square(-2)

    def test_height_type_error(self):
        """test to see if typeError is raised"""
        with self.assertRaises(TypeError):
            Rectangle(2, 2.5)

    def test_width_type_error(self):
        """test to see if valueError is raised wrong width"""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_x_type_error(self):
        """test for type error"""
        with self.assertRaises(TypeError):
            Square(1, 2.5)

    def test_x_value_error(self):
        """test for x value error"""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_y_type_error(self):
        """test for correct y type"""
        with self.assertRaises(TypeError):
            Square(1, 1, -2.5)

    def test_y_value_error(self):
        """test for correct y value"""
        with self.assertRaises(ValueError):
            Square(1, 2, -2)

    def test_area(self):
        """test to see if area is correct"""
        t = Square(4)
        self.assertEqual(t.area(), 16)

    def test_display_with_hash(self):
        """test to see if display print expected output"""
        t = Square(3)
        capture_output = io.StringIO()
        sys.stdout = capture_output
        t.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capture_output.getvalue(), "###\n###\n###\n")

    def test_display_with_axis(self):
        """test display of rectangle with axis"""
        r = Square(3, 2, 2)
        capture_output = io.StringIO()
        sys.stdout = capture_output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capture_output.getvalue(), "\n\n  ###\n  ###\n  ###\n")

    def test_string(self):
        """test if the string representation is right"""
        t = Square(1, 3, 2, 12)
        self.assertEqual(str(t), "[Rectangle] (12) 3/2 - 1")

    def test_string_x_zero(self):
        """test if the string representation is rigth y=0"""
        r = Square(3, 0, 2)
        capture_output = io.StringIO()
        sys.stdout = capture_output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capture_output.getvalue(), "\n\n###\n###\n###\n")

    def test_string_y_zero(self):
        """test if the string representation is rigth y=0"""
        r = Square(3, 2, 0)
        capture_output = io.StringIO()
        sys.stdout = capture_output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capture_output.getvalue(), "  ###\n  ###\n  ###\n")

    def test_update(self):
        """test for all update"""
        r = Square(3, 2, 0)
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