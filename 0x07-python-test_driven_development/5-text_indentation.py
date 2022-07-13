#!/usr/bin/python3
""" defines a function that print a text with identation"""


def text_indentation(text):
    """include 2 new lines where there is ., ?, and : """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")
    text_lines = text.split("\n\n")
    text_lines = [i.strip()+"\n\n" for i in text_lines]
    text = ''.join(text_lines)
    print(text.strip(), end='')
