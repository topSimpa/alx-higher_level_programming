#!/usr/bin/python3
"""This script that takes in a URL and an email,
   sends a POST request to the passed URL with the email as a parameter,
   and displays the body of the response
"""
if __name__ == "__main__":
    import sys
    import requests

    dat = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], data=data)
    print(req.text)
