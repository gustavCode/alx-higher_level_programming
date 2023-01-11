#!/usr/bin/python3
"""
A module that returns an object represented
by a JSON string
"""
from json import loads


def from_json_string(my_str):
    """
    Returns an object represented by JSON

    Args:
        my_str (any): JSON string

    Returns:
        an object represented by JSON string
    """

    return loads(my_str)
