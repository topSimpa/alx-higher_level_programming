#!/usr/bin/python3
position = 0
while position < 26:
    if position % 2 == 0:
        print("{}".format(chr(122 - position)), end="")
    else:
        print("{}".format(chr(90 - position)), end="")
    position += 1
