#!/usr/bin/python3
""" defines a function that serialize class"""


def class_to_json(obj):
    """returns a dictionary format of serialize object"""
    return ((obj.__dict__))
