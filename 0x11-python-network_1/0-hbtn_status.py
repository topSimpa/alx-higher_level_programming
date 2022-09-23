#!/usr/bin/python3
"""This script fetches a url:
       https://alx-intranet.hbtn.io/status
"""

from urllib.request import urlopen

with urlopen('https://alx-intranet.hbtn.io/status') as request:
    body = request.read()

print(f"Body response:\n\t- type: {type(body)}\n\t- content: {body}\n\t\
- utf8 content: {body.decode()}")
