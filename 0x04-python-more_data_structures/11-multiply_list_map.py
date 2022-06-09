#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    if my_list:
        def mul2(x): return x * number
        return list(map(mul2, my_list))
    return my_list
