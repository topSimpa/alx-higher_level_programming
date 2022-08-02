#!/usr/bin/python3
""" star a new class calle BaseGeometry """


class BaseGeometry:
    """An empty class"""
    pass

    def area(self):
        """ raises an except """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
