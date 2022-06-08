#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        rep_list = [replace if elem == search else elem for elem in my_list]
        return rep_list
    return my_list
