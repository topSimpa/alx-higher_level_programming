#!/usr/bin/python3
""" more flexible instance check"""


def is_kind_of_class(obj, a_class):
    """ returns a bool that is
        True- obj is an instance of a_class or its subclass
        False - obj is not an instance of a_class or its subclass
    """
    return (isinstance(obj, a_class))
