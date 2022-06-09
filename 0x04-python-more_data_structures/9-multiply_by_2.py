#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    times2_dict = {}
    for key in a_dictionary.keys():
        times2_dict[key] = a_dictionary[key] * 2
    return times2_dict
