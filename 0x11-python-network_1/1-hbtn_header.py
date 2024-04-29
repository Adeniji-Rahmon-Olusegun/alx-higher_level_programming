#!/usr/bin/python3
"""
sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""

if __name__ == "__main__":
    import sys
    import urllib.request as url

    with url.urlopen(sys.argv[1]) as res:
        headers = res.headers
        if "X-Request-Id" in headers:
            print((headers["X-Request-Id"]))
