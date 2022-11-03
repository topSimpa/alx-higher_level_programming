#!/usr/bin/python3
""" defines the very first class of this package"""
import json


class Base:
    """ This is a prototype that serve as a base to other classes"""

    __nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """return a json format of list of dictionary"""
        if not list_dictionaries:
            return (json.dumps([]))
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """help to write the JSON string to a file"""
        with open("{}.json".format(cls.__name__), 'w') as file:
            if not list_objs:
                list_objs = []
            list_dict = []
            for i in list_objs:
                list_dict.append(i.to_dictionary())
            file.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """deserialize the json list of dictionary"""
        if not json_string:
            return (json.loads('[]'))
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """create an object of class from a dictionary"""
        if cls.__name__ == "Rectangle":
            instance = cls(2, 3)
        elif cls.__name__ == "Square":
            instance = cls(3)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """create/loads a list of objects from files"""
        with open("{}.json".format(cls.__name__), 'r') as file:
            json_string = file.readline()
            list_dict = Base.from_json_string(json_string)
            list_obj = []
            print(list_dict)
            for i in list_dict:
                list_obj.append(cls.create(**i))
        return list_obj

    def __init__(self, id=None):
        """ initializes instance attributes"""

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_object
