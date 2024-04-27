#!/usr/bin/python3
"""
Module of a function to fetch a URL and print the body
"""
import requests


def fetch_url(url: str):
    """
    Fetches data from the provided url and prints the body
    """
    response = requests.get(url)
    body = response.text
    print("Body response:")
    print("\t- type: {}".format(body.__class__))
    print("\t- content: {}".format(body))


if __name__ == "__main__":
    fetch_url("https://alx-intranet.hbtn.io/status")
