#!/usr/bin/python3
"""raise exceeption without try except"""


def add_attribute(obj, attr, val):
    """safely add atribute to object"""
    if '__dict__' in dir(obj):
        setattr(obj, attr, val)
    else
        raise(TypeError('cant add new attribute'))
