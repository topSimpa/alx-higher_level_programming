#!/usr/bin/python3
""" we define a square class with one attribute
size which is peculiar to different sqaure object
"""


class Square:
    """This class initializes an attribute size on each instance
    using the init function
    """
    def __init__(self, size):
        self.__size = size
