#!/usr/bin/python3
""" This Script takes your github credentials and displays
    your id.
    Usage: ./10-my_github.py <username> <password>or<token>
"""

if __name__ == '__main__':
    import requests
    import sys

    cred = tuple(sys.argv[1:])
    profile = requests.get('https://api.github.com/user', auth=cred)
    print(profile.json().get('id'))
