#!/usr/bin/python3
def roman_to_int(roman_str):
    if roman_str and type(roman_str) == str:
        ro = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        for id in range(len(roman_str)):
            if (roman_str[id] in ro):
                if id == 0:
                    sum = sum + ro[roman_str[id]]
                elif (ro[roman_str[id]] > ro[roman_str[id - 1]]):
                    sum += -(2 * ro[roman_str[id - 1]] - ro[roman_str[id]])
                else:
                    sum += ro[roman_str[id]]
        return sum
    return 0
