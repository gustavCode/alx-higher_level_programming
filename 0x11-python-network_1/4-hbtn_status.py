#!/usr/bin/python3
"""
Fetches the URL: https://intranet.hbtn.io/status
with `requests` module
"""

import requests


if __name__ == "__main__":
    reqs = requests.get('https://intranet.hbtn.io/status')

    print('Body response:')
    print('\t- type: {_type}'.format(_type=type(reqs.text)))
    print('\t- content: {_content}'.format(_content=reqs.text))
