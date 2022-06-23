#!/usr/bin/python3
""" we define a square class with one attribute
size which is peculiar to different sqaure object
size is always be an integer greater than 0
"""


class Square:
    """This class initializes an attribute size on each instance
    using the init function, condition to set size
    """
    def __init__(self, size=0):
        if type(size) == "int":
            self.__size = size
        elif size < 0:
            try:
                raise ValueError
            except ValueError:
                print("size must be >= 0")
        else:
            try:
                raise TypeError
            except TypeError:
                print("size must be an integer")
