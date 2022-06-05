#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum_one, sum_two = 0, 0
    if len(tuple_a) >= 2:
        sum_one += tuple_a[0]
        sum_two += tuple_a[1]
    elif len(tuple_a) == 1:
        sum_one += tuple_a[0]

    if len(tuple_b) >= 2:
        sum_one += tuple_b[0]
        sum_two += tuple_b[1]
    elif len(tuple_b) == 1:
        sum_one += tuple_b[0]
    return (sum_one, sum_two)
