#!/usr/bin/env python3

""" defines a class that inherint from the list class"""


class MyList(list):
    """ This class is a child of the python list.
    it has a new method print_sorted """

    def print_sorted(self):
        """ print the list in ascending sorted format """
        r = self.copy()
        r.sort()
        print(r)
