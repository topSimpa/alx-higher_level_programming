#!/usr/bin/python3
""" describe a class Student """


class Student:
    """ The student class """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return the json dict representation of an object"""
        js = {}
        if type(attrs) == list:
            for i in attrs:
                if i in self.__dict__.keys():
                    js[i] = self.__dict__[i]
            return (js)
        return (self.__dict__)
