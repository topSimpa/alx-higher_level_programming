#!/usr/bin/python3
"""This script fetches a url passed to it as an argument:
   and displays the value of the X-Request-Id variable
   found in the header of the response
"""
if __name__ == "__main__":
    import sys
    from urllib.request import urlopen

    with urlopen(sys.argv[1]) as request:
        print(request.getheader('X-Request-Id'))
