#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        withoutc = ""
        for char in my_string:
            if char != 'c' and char != 'C':
                withoutc += char
    return withoutc
