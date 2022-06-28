#!/usr/bin/python3
"""
This is the documentation for an empty Rectangle class
"""


class Rectangle:
    """ Rectangle class that has two private attribute width, height """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Calculate the area of the Rectangle object"""
        return(self.width * self.height)

    def perimeter(self):
        """ Calculate the perimeter of the Rectangle object"""
        if self.width == 0 or self.height == 0:
            return (0)
        else:
            return (2*(self.width + self.height))
