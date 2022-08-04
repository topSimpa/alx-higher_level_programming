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
        self.size = size

    """ This is the method used to get class attribute size"""
    @property
    def size(self):
        return self.__size

    """This is the method used to set the class attribute size"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """ The method to get the area of the square"""

    def area(self):
        return (self.__size * self.__size)

    def __eq__(self, value):
        if self.area() == value.area():
            return True
        return False

    def __ne__(self, value):
        return not (self.__eq__(value))

    def __lt__(self, value):
        if self.area() < value.area():
            return True
        return False

    def __gt__(self, value):
        if self.area() > value.area():
            return True
        return False

    def __le__(self, value):
        if self.area() <= value.area():
            return True
        return False

    def __ge__(self, value):
        if self.area() >= value.area():
            return True
        return False
