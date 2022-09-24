#!/usr/bin/python3
"""This script fetches a url:
       https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import requests
    body = requests.get('https://alx-intranet.hbtn.io/status')
    print(f"Body response:\n\t- type: {type(body.text)}\n\t\
- content: {body.text}")
