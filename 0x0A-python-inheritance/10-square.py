#!/usr/bin/python3
"""this defines the rectangle class"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ this class is a child of BaseGeometry"""

    def __init__(self, size):
        """initializes the class attribute"""
        super().__init__(size, size)
        self.__size = size
