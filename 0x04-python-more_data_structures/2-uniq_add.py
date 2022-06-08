#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        uniq_list = [i for i in my_list if my_list.count(i) == 1]
        return sum(uniq_list)
    return my_list
