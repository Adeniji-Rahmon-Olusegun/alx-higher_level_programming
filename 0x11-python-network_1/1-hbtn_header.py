#!/usr/bin/python3

import sys
import urllib.request as url

with url.urlopen(sys.argv[1]) as res:
    print(res.getheader("X-Request-Id"))
