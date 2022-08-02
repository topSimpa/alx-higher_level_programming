#!/usr/bin/python3
""" defines a rebel MyInt """


class MyInt(int):
    """a rebel integer class"""
    def __eq__(self, value):
        return (super().__ne__(value))

    def __ne__(self, value):
        return (super().__eq__(value))
