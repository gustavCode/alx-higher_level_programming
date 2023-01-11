#!/usr/bin/python3
"""
Wrints an object to text file, using
a JSON representation
"""
from json import dumps


def save_to_json_file(my_obj, filename):
    """
    Writes an object to text file, using a
    JSON representation

    Args:
        my_obj (any): objec to write
        filename : text file
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(dumps(my_obj))
