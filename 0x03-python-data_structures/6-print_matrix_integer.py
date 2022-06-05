#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if row:
            for column in row:
                if column == row[-1]:
                    print("{:d}".format(column))
                else:
                    print("{:d}".format(column), end=" ")
        else:
            print("")
