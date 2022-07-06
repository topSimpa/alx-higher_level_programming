#!/usr/bin/python3
"""defines the write file function"""


def write_file(filename="", text=""):
    """This function writes to a file and returns word-count"""
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
