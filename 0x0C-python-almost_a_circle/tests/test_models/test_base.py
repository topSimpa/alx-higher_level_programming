#!/usr/bin/python3
""" defines test cases for base class """

import os
import json
from unittest import TestCase
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BaseTestCases(TestCase):
    """ Base class initialization checks"""

    def test_instance(self):
        """ test all proper instance of the base class """

        self.assertIsInstance(Base(2), Base)

    def test_id_assigned(self):
        """ test if id was assigned when base is created with an input"""
        self.assertEqual(Base(2).id, 2)
        a, b = Base(), Base()
        self.assertEqual(a.id + 1, b.id)


class BaseIOTestCases(TestCase):
    """ Test for serialization and deserialization """

    def setUp(self):
        """setup class for use"""
        global a, b, c, d
        a = Square(2)
        b = Square(4)
        c = Rectangle(3, 4)
        d = Rectangle(5, 6)

    def test_to_json_string(self):
        """test if to json_string return json string"""
        all_list = [a.to_dictionary(), b.to_dictionary(),
                    c.to_dictionary(), d.to_dictionary()]
        empty = []
        self.assertEqual(Base.to_json_string(all_list), json.dumps(all_list))
        self.assertEqual(Base.to_json_string(empty), json.dumps(empty))

    def test_save_to_file(self):
        """test to see if json type was save in file"""
        square_list = [a, b]
        rectangle_list = [c, d]
        s_listdict = [a.to_dictionary(), b.to_dictionary()]
        r_listdict = [c.to_dictionary(), d.to_dictionary()]
        empty = []

        # test for square data type
        Square.save_to_file(square_list)
        with open('Square.json', 'r') as file:
            self.assertEqual(file.readline(), json.dumps(s_listdict))

        # test for rectangle data type
        Rectangle.save_to_file(rectangle_list)
        with open('Rectangle.json', 'r') as file:
            self.assertEqual(file.readline(), json.dumps(r_listdict))

        # test for saving an empty list
        Square.save_to_file(empty)
        with open('Square.json', 'r') as file:
            self.assertEqual(file.readline(), json.dumps(empty))

    def test_from_json_string(self):
        """test to see if json string is converted to dictionary"""
        all_list = [a.to_dictionary(), b.to_dictionary(),
                    c.to_dictionary(), d.to_dictionary()]
        empty = []
        self.assertEqual(Base.from_json_string(json.dumps(all_list)), all_list)
        self.assertEqual(Base.from_json_string(json.dumps(empty)), empty)
        self.assertEqual(Base.from_json_string(None), empty)
