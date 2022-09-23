#!/usr/bin/python3
"""This script fetches a url:
       https://alx-intranet.hbtn.io/status
"""

from urllib.request import urlopen

with urlopen('https://alx-intranet.hbtn.io/status') as request:
    body = request.read()

print(f"Body response:\n    - type: {type(body)}\n\
    - content: {body}\n    - utf8 content: {body.decode()}")
