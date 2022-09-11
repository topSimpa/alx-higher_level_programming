#!/usr/bin/python3
import sys

print(sys.argv)

print("{} {} '{}' ".format(sys.argv[1], sys.argv[2], sys.argv[3]))

for i in sys.argv:
    print(i)
