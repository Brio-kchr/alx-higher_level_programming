#!/usr/bin/python3
"""
Module of a function to fetch a URL and retrieve a header value
"""
import requests


def get_header(url: str, header_var: str):
    """
    Fetches data from the provided url and prints a header value
    """
    response = requests.get(url)
    if header_var in response.headers.keys():
        return response.headers[header_var]
    return None


if __name__ == "__main__":
    from sys import argv

    header = get_header(argv[1], "X-Request-Id")
    print(header)
