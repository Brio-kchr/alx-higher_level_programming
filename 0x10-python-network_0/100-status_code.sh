#!/bin/bash
# Sends a request to a URL passed as an arg, and displays only the
# status code of the response
curl --silent --output /dev/null --write-out "%{http_code}" "$1" 
