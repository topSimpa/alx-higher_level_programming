#!/usr/bin/python3
"""module defines a function that returns a list of attributes"""


def lookup(obj):
    """ returns all attribute and method of an object"""
    return (dir(obj))
