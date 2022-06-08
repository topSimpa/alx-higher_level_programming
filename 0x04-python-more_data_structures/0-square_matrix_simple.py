#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        square = lambda x: [i ** 2 for i in x]
        matrixSquare = [square(elem) for elem in matrix]
        return matrixSquare
    return matrix
