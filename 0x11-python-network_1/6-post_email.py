#!/usr/bin/python3
"""
Takes a url and email, and sends a POST request to the
passed URL with email as param and displays the body
of the response
"""
import requests


def post_url(url: str, data: dict):
    """
    Posts data to the provided url and prints the body
    """
    response = requests.get(url, json = data)
    body = response.text
    print("Body response:")
    print("\t- type: {}".format(body.__class__))
    print("\t- content: {}".format(body))


if __name__ == "__main__":
    from sys import argv

    data = {"email": argv[2]}
    post_url(argv[1], data)
