#!/usr/bin/python3
""" takes in argument and write it to a json file"""
import sys
from os.path import exists
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file


if len(sys.argv) > 1:
    arr = load_from_json_file("add_item.json")
    for i in (sys.argv[1:]):
        if type(arr) == list:
            arr.append(i)
        else:
            arr = []
    save(arr, "add_item.json")
elif exists("add_item.json") == False:
    save([], "add_item.json")
