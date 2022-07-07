#!/usr/bin/python3
""" define the reads json_file function"""
import json as js


def load_from_json_file(filename):
    """ returns python object from jsonread"""
    with open(filename, "r") as f:
        return (js.load(f))
