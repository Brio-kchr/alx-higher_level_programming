#!/usr/bin/python3
"""
Module of a function to fetch a URL and retrieve a header value
"""
import urllib.request


def get_header(url: str, header_var: str):
    """
    Fetches data from the provided url and prints a header value
    """
    with urllib.request.urlopen(url) as response:
        return response.headers.get(header_var)


if __name__ == "__main__":
    from sys import argv

    header = get_header(argv[1], "X-Request-Id")
    print(header)
