#!/usr/bin/python3
""" This python script takes 2 arguments in order to
solve this challenge:
    list 10 commits from the recent to oldest of the repository

    Usage: ./100-github_commits.py <repository name> <owner name>
"""

if __name__ == '__main__':
    import sys
    import requests

    a = sys.argv[1:]
    coms = requests.get(f"https://api.github.com/repos/{a[1]}/{a[0]}/commits")
    top_ten = coms.json()[:10]

    for i in top_ten:
        print(f"{i.get('sha')}:", end=" ")
        print(i.get('commit').get('author').get('name'))
