#!/usr/bin/python3
""" defines the very first class of this package"""


class Base:
    """ This is a prototype that serve as a base to other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes instance attributes"""

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
