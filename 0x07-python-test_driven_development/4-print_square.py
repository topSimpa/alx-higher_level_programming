#!/usr/bin/python3
""" defines the function that uses # to print a square """


def print_square(size):
    """print a square by size using #: size must be int """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
