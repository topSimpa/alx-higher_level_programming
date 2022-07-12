#!/usr/bin/python3
""" This module defines a function that adds two integer """


def add_integer(a: int or float, b=98):
    """ adds two integer together and returns their sum"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
