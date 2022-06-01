#!/usr/bin/python3
def print_last_digit(number):
    print(int((str(number))[-1]), end="")
    return (int((str(number))[-1]))
print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
