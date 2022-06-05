#!/usr/bin/python3
def no_c(my_string):
    if my_string and type(my_string) == str:
        withoutc = ""
        for char in my_string:
            if char != 'c' and char != 'C':
                withoutc += char
    return withoutc
