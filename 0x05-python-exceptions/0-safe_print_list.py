#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if (x and my_list):
        count = 0
        for index in range(x):
            try:
                print(my_list[index], end="")
            except IndexError:
                count += 1
        print("")
        return (x - count)
    return 0
