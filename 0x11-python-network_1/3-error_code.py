#!/usr/bin/python3
"""
Module of a function to fetch data from a URL with error handling
"""
import urllib.request
import urllib.error


def fetch_url(url: str):
    """
    Fetches data from the provided url and prints the body
    """
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    from sys import argv

    fetch_url(argv[1])
