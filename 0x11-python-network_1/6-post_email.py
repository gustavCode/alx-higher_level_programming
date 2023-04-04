#!/usr/bin/python3
"""
Takes in a URL and an email address, sends a
POST request to the passed URL with the email
as a parameter, and finally displays the body
of the response.
"""

from sys import argv
import requests


if __name__ == "__main__":
    pay_load = {'email': argv[2]}
    reqs = requests.post(argv[1], data=pay_load)

    print(reqs.text)
