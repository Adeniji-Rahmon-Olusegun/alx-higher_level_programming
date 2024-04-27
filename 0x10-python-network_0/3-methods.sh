#!/bin/bash
#  script that takes in a URL and displays all HTTP methods the server will accept
curl -sX -i OPTIONS $1 | grep -i allow
