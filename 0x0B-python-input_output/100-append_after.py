#!/usr/bin/python3
"""defines a search and append function"""


def append_after(filename="", search_string="",
                 new_string=""):
    """search and insert new_string to next line of file"""
    with open(filename, 'r') as file:
        old = file.readlines()
        edit = []
        for i in old:
            edit.append(i)
            if search_string in i:
                edit.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(edit)
