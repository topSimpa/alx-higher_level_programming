#!/usr/bin/python3
""" defines a rebel MyInt """

class MyInt(int):
    """a rebel integer class"""

    def __eq__(self):
       if self == 3:
           return (False)
       return (True)

    def __ne__(self):
        if self != 3:
           return (False)
        return (True)
