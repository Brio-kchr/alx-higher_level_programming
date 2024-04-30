#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to a URL with
the letter as a param
"""
import requests


def post_url(url: str, data: dict):
    """
    Posts data to the provided url and prints the body
    """
    response = requests.post(url, data = data)
    if (response.status_code == 204) or (len(response.text) == 0):
        print("No result")
        return
    try:
        response.json()
    except Exception:
        print("Not a valid JSON")
        return
    print("[{}] {}".format(res["id"], res["name"]))

if __name__ == "__main__":
    from sys import argv

    data = {"q": ""}
    if len(argv) > 1:
        data.update({"q": argv[2]})
    post_url("http://0.0.0.0:5000/search_user", data)
