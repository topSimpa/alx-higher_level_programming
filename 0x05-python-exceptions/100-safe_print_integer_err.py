#!/usr/bin/python3
"""print an integer safely"""
import sys


def safe_print_integer_err(value):
    """print a number or error"""
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
