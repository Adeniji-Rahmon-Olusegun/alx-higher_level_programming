#!/usr/bin/python3

"""
script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


if __name__ == "__main__":
    import sys
    import requests

    if len(sys.argv) == 2:
        alpb = sys.argv[1]
    else:
        alpb = ""

    url = "http://0.0.0.0:5000/search_user"
    post_data = {'q': alpb}

    res = requests.post(url, data=post_data)

    try:
        data = res.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
