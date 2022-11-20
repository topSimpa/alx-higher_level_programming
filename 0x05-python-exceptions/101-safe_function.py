#!/usr/bin/python3
"""execute a function safely"""
import sys


def safe_function(fct, *args):
    """return a value or print error on execution"""
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
