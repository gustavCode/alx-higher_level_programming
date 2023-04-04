#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)
with `requests` module.
"""

from sys import argv
import requests


if __name__ == "__main__":
    reqs = requests.get(argv[1])

    if reqs.status_code >= 400:
        print('Error code:', reqs.status_code)
    else:
        print(reqs.text)
