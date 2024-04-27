#!/bin/bash
#  script that takes in a URL and displays all HTTP methods the server will accept
curl -s -i -X OPTIONS $1 -L | grep -i "allow" | cut -d ":" -f2 | tr -d '[:space:]'
