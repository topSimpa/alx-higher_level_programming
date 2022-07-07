#!/usr/bin/python3
""" define the write json_string to file function"""
import json as js


def save_to_json_file(my_obj, filename):
    """ this convert python obj into json string and write to file"""
    with open(filename, "w") as f:
        js.dump(my_obj, f)
