#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if (my_list):
        lent = len(my_list)
        while lent > 0:
            print("{:d}".format(my_list[lent - 1]))
            lent -= 1
