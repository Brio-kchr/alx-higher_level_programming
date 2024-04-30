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
    response = requests.post(url, json = data)
    print(response.text)

if __name__ == "__main__":
    from sys import argv

    data = {"email": argv[2]}
    post_url(argv[1], data)
