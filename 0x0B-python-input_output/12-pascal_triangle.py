#!/usr/bin/python3
""" returns a pascal triangle """


def pascal_triangle(n):
    coefs = []
    if n <= 0:
        return coefs
    j = 0
    while j < n:
        new = []
        i = 0
        while i <= j:
            if i == 0:
                new.append(1)
            elif i == j:
                new.append(1)
            else:
                new.append(coefs[j - 1][i - 1] + coefs[j - 1][i])
            i += 1
        coefs.append(new)
        j += 1
    return coefs
