#!/usr/bin/python3
""" defines test cases for base class """

import os
from unittest import TestCase
from models.base import Base
from models.rectangle import Rectangle


class BaseTestCases(TestCase):
    """ This class define function test cases """

    def test_instance(self):
        """ test all proper instance of the base class """

        self.assertIsInstance(Base(2), Base)

    def test_id_assigned(self):
        """ test if id was assigned when base is created with an input"""
        self.assertEqual(Base(2).id, 2)
        #self.assertEqual(Base().id, 1)
        #self.assertEqual(Base().id, 2)
        #self.assertRaises(AttributeError, Base(2).__nb_objects)
        #self.assertIsInstance(Base(), Base)

    def test_json_string(self):
        """test json method"""
        r1 = Rectangle(10, 7, 2, 8, 5)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertAlmostEqual(json_dictionary, '{}'.format([dictionary]))
