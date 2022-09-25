#!/usr/bin/python3
"""tries to get the json format of post reques
   Usage: ./8-json_api.py <letter>
"""
import requests
import sys

if __name__ == '__main__':
    letters = {'letter': sys.argv[0])
    resp = requests.post('http://0.0.0.0:5000/search_user', data=letters)

    try:
        js = resp.json()
        if js == {}:
            print("No result")
        else:
            print(f"[{js.get('id')}] {js.get('name')}")
    except Exception:
        print("Not a valid JSON")
