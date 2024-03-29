#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL
and displays the value of the `X-Request-Id`
variable found in the header of the response.
"""

from sys import argv
import requests


if __name__ == "__main__":
    reqs = requests.get(argv[1])

    print(reqs.headers.get('X-Request-Id'))
