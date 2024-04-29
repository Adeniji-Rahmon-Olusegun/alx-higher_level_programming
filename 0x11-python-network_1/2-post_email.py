#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    import sys
    import urllib.parse as urlp
    import urllib.request as url

    key_val = {"email": sys.argv[2]}

    data = urlp.urlencode(key_val)
    data = data.encode('ascii')
    post_request = url.Request(sys.argv[1], data)

    with url.urlopen(post_request) as res:
        page = res.read()
        print(page.decode('utf-8'))
