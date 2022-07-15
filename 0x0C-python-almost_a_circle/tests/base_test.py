#!/usr/bin/python3
""" defines test cases for base class """

from unittest import TestCase
from models.base import Base


class BaseTestCases(TestCase):
    """ This class define function test cases """

    def all_test(self):
        self.assertIsInstance(Base(2), Base)
        self.assertEqual(Base(2).id, 2)
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, Base().__nb_objects)
        self.assertEqual(Base(2).__nb_objects, 2)
        self.assertIsInstance(Base(), Base)
