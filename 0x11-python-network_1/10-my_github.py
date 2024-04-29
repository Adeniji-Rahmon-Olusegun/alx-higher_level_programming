#!/usr/bin/python3

"""
script that takes your GitHub credentials 
(username and password) and uses the GitHub API to display your id
"""


if __name__ == "__main__":
    import sys
    import requests

    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    res = requests.get(url, auth=(username, password))

    if res.status_code == 200:
        json_data = res.json()
        print(f"{json_data['id']}")
    else:
        print(None)
