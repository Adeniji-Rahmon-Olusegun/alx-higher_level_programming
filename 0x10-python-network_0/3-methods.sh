#!/bin/bash
#  script that takes in a URL and displays all HTTP methods the server will accept
curl -siX OPTIONS $1 | grep -i allow | cut -d ":" -f2 | tr -d '[:space:]'
