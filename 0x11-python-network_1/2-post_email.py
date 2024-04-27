#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in the header
of the response.
"""
import urllib.request
import urllib.parse
from sys import argv

data_post = {}
data_post.update({"email": argv[2]})

data = urllib.parse.urlencode(data_post).encode('ascii')
request = urllib.request.Request(argv[1], data)

with urllib.request.urlopen(request) as response:
    print(response.read().decode("utf-8"))
