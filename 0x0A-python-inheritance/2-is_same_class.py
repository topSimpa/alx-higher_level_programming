#!/usr/bin/python3
""" This is the module for instance check"""


def is_same_class(obj, a_class):
    """ Returns a boolean. The bool returned
        True-if obj is a_class instance,
        False-if obj is not a_class instance"""
    return (isinstance(obj, a_class) and type(obj) == a_class)
