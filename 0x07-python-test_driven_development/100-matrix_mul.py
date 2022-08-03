#!/usr/bin/python3
""" defines a function for matrix multiplication """


def matrix_mul(m_a, m_b):
    """multiplies matrix a m_a by matrix b m_b"""

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if not m_a:
        raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")
    list_check = list(map(lambda x: 1 if (type(x) is list) else 0, m_a))
    list_checkb = list(map(lambda x: 1 if (type(x) is list) else 0, m_b))
    if len(m_a) == 1 and not m_a[0]:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 1 and not m_b[0]:
        raise ValueError("m_b can't be empty")
    if sum(list_check) != len(m_a):
        raise TypeError("m_a must be a list of list")
    if sum(list_checkb) != len(m_b):
        raise TypeError("m_b must be a list of list")

    def type_check(x):
        if type(x) in [int, float]:
            return 1
        return 0

    for i in range(len(m_a)):
        if sum(list(map(type_check, m_a[i]))) != len(m_a[i]):
            raise TypeError("m_a should contain only integers or floats")
    for i in range(len(m_b)):
        if sum(list(map(type_check, m_b[i]))) != len(m_b[i]):
            raise TypeError("m_b should contain only integers or floats")

    row_len = (len(m_a[0]), len(m_b[0]))
    row_check = list(map(lambda x: 1 if (len(x) == row_len[0]) else 0, m_a))
    row_checkb = list(map(lambda x: 1 if (len(x) == row_len[1]) else 0, m_b))
    if sum(row_check) != len(m_a):
        raise TypeError("each row of m_a must be of the same size")
    if sum(row_checkb) != len(m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for a in m_a:
        new_row = []
        for b in range(len(m_b[0])):
            ins = 0
            for i in range(len(m_b)):
                ins += a[i] * m_b[i][b]
            new_row.append(ins)
        result.append(new_row)
    return (result)
