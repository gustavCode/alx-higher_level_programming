#!/usr/bin/python3
"""
A module to return JSON of object
"""
from json import dumps


def to_json_string(my_obj):
    """
    Returns JSON representation of an object

    Args:
        my_obj (str): strin

    Returns:
        JSON representation
    """

    return dumps(my_obj)
