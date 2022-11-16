#!/usr/bin/python3
""" describe a class Student """


class Student:
    """ The student class """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return the desired attribute of an objects as dict"""
        js = {}
        if type(attrs) == list:
            for i in attrs:
                if i in self.__dict__.keys():
                    js[i] = self.__dict__[i]
            return (js)
        return (self.__dict__)

    def reload_from_json(self, json):
        """update an object with the content of json"""
        for attr, val in json.items():
            setattr(self, attr, val)
