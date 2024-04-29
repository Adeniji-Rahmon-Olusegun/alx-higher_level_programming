#!/usr/bin/python3
"""
manage urllib.error.HTTPError exceptions and print: Error code:
followed by the HTTP status code
"""

if __name__ == "__main__":
    import sys
    import urllib.request as url
    import urllib.error as urle

    request = url.Request(sys.argv[1])

    try:
        with url.urlopen(request) as res:
            data = res.read()
            print(data.decode('utf-8'))
    except urle.HTTPError as e:
        print(f"Error code: {e.code}")
