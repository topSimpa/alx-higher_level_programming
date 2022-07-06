#!/usr/bin/python3
""" This defines read_file """


def read_file(filename=""):
    """ reads from a text file passed in as input """
    if filename:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
            print(text, end="")
