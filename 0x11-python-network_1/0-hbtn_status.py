#!/usr/bin/python3
"""
Fetches the URL: https://intranet.hbtn.io./status
"""

import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        body = response.read()
        utf8_content = body.decode('utf-8')

        print('Body response:')
        print('\t- type: {_type}'.format(_type=type(body)))
        print('\t- content: {_content}'.format(_content=body))
        print('\t- ut8 content: {_utf8_c}'.format(_utf8_c=utf8_content))
