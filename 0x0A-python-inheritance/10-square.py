#!/usr/bin/python3
"""this defines the rectangle class"""


Rectangle = __import__("9-rectangle").BaseGeometry


class Square(Rectangle):
    """ this class is a child of BaseGeometry"""

    def __init__(self, size):
        """initializes the class attribute"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ returns the area of Square"""
        return (self.__size ** 2)
