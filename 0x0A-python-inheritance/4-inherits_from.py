#!/usr/bin/python3
""" the subclass instance checker """


def inherits_from(obj, a_class):
    """checks if obj is a subclass instance"""
    return (isinstance(obj, a_class) and type(obj) != a_class)
