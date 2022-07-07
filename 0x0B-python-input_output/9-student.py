#!/usr/bin/python3
""" describe a class Student """


class Student:
    """ The student class """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return the json dict representation of an object"""
        return (self.__dict__)
