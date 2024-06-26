#!/usr/bin/python3

"""
script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""


if __name__ == "__main__":
    import sys
    import requests

    key_val = {"email": sys.argv[2]}

    res = requests.post(sys.argv[1], key_val)

    print(res.text)
