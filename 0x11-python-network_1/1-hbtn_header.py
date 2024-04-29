#!/usr/bin/python3

import sys
import urllib.request as url

with url.urlopen(sys.argv[1]) as res:
    headers = res.headers
    if "X-Request-Id" in headers:
        print(headers["X-Request-Id"])
