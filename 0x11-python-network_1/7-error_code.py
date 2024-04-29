#!/usr/bin/python3

"""
manage urllib.error.HTTPError exceptions and print: Error code:
followed by the HTTP status code
"""


if __name__ == "__main__":
    import sys
    import requests

    res = requests.get(sys.argv[1])

    if res.status_code >= 400:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)
