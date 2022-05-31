#!/usr/bin/python3
asciiCode = 0
while asciiCode < 26:
    if asciiCode != 4 and asciiCode != 16:
        print("{}".format(chr(97 + asciiCode)), end="")
    asciiCode += 1
