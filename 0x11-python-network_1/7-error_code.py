#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL
   and displays the body of the response (decoded in utf-8)

   Usage: ./7-error_code <url>
"""
if __name__ == "__main__":
    import sys
    import requests

    resp = requests.get(sys.argv[1])
    if resp.status_code >= 400:
        print(f"Error code: {resp.status_code}")
    else:
        #print(resp.text)
        print(resp.status_code)
