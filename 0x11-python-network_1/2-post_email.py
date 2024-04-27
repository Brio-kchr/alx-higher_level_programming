#!/usr/bin/python3
"""
Module of a function to post data to a URL
"""
import urllib.request
import urllib.parse


def post_data(url: str, dict_data: dict):
    """
    Posts data to the provided url and prints the body
    """
    data = urllib.parse.urlencode(dict_data).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))


if __name__ == "__main__":
    from sys import argv

    data = {}
    data.update({"email": argv[2]})
    post_data(argv[1], data)
