#!/usr/bin/python3
"""this defines the rectangle class"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ this class is a child of BaseGeometry"""

    def __init__(self, width, height):
        """initializes the class attribute"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ returns the area of rectangle"""
        return (self.__height * self.__width)

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")
