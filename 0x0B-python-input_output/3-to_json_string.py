#!/usr/bin/python3
""" defines obj_to_json function"""
import json as js


def to_json_string(my_obj):
    """ changes obj to json string"""
    return (js.dumps(my_obj))
