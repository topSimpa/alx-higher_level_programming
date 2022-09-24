#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL
   and displays the body of the response (decoded in utf-8)

   Usage: ./3-error_code <url>
"""
if __name__ == "__main__":
    import sys
    from urllib.request import urlopen
    from urllib.error import HTTPError

    try:
        with urlopen(sys.argv[1]) as request:
            print(request.read().decode('utf-8'))
    except HTTPError as e:
        print(f"Error code: {e.code}")
