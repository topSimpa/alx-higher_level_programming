#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        unwanted = []
        if (value in a_dictionary.values()):
            for key in a_dictionary:
                if a_dictionary[key] == value:
                    unwanted.append(key)
            for key in unwanted:
                del a_dictionary[key]
    return a_dictionary
