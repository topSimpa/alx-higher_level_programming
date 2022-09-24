#!/usr/bin/python3
"""This script that takes in a URL and an email,
   sends a POST request to the passed URL with the email as a parameter,
   and displays the body of the response
"""
if __name__ == "__main__":
    import sys
    from urllib.request import urlopen, Request

    req = Request(sys.argv[1], (sys.argv[2]).encode)
    with urlopen(req) as request:
        print(request.read())
