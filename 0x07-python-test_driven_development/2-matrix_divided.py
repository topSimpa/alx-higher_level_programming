#!/usr/bin/python3
""" defines a function that takes a matrix and divide it """


def matrix_divided(matrix, div):
    """ divides matrix by div """
    if type(matrix) is list and matrix:
        r = sum([1 for i in matrix if type(i) in [int, float, list]])
        if r == len(matrix):
            if sum([1 for i in matrix if type(i) is list]) == len(matrix):
                r = sum([1 for i in matrix if len(i) == len(matrix[0])])
                if r != len(matrix):
                    raise TypeError("Each row of the matrix\
 must have the same size")
            elif type(div) in [int, float] and div != 0:
                return list(map(lambda x: round(x / div, 2), matrix))
            elif div == 0:
                raise ZeroDivisionError("division by zero")
            else:
                raise TypeError("div must be a number")
        else:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    else:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
