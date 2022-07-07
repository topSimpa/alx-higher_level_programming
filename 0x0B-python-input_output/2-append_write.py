#!/usr/bin/python3
"""defines the write file function"""


def append_write(filename="", text=""):
    """This function writes to a file end and returns word-count"""
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
