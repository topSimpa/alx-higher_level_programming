#!/usr/bin/python3
fDigit = 0
while fDigit < 10:
    sDigit = 0
    while sDigit < 10:
        if sDigit > fDigit:
            if not (fDigit == 8 and sDigit == 9):
                print("{}{},".format(fDigit, sDigit), end=" ")
            else:
                print("{}{}".format(fDigit, sDigit))
        sDigit += 1
    fDigit += 1
