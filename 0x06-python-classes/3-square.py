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
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """This method returns the area of a square
       which size ** size """

    def area(self):
        return (self.__size * self.__size)
