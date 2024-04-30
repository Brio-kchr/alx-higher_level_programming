#!/usr/bin/python3
"""
Takes a url, sends a request and displays body of the response
"""
import requests


def req_url(url: str):
    """
    Checks http status code before displaying response body
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)

if __name__ == "__main__":
    from sys import argv

    req_url(argv[1])
