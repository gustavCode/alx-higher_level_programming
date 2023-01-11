#!/usr/bin/python3
"""
Module that creates an object from a JSON file
"""
from json import loads


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file

    Args:
        filename : JSON file

    Returns:
        object created
    """

    with open(filename, encoding='utf-8') as f:
        return loads(f.read())
