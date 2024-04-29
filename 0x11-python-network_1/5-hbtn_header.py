#!/usr/bin/python3
"""
sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""

if __name__ == "__main__":
    import sys
    import requests

    res = requests.get(sys.argv[1])

    value = res.headers["X-Request-Id"]
    print(value)
