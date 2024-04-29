#!/usr/bin/python3

import urllib.request as url

with url.urlopen("https://alx-intranet.hbtn.io/status") as res:
    info = res.read()
    print("Body response:")
    print(f"\t- type: {type(info)}")
    print(f"\t- content: {info!r}")
    print(f"\t- utf8 content: {info.decode('utf-8')}")
