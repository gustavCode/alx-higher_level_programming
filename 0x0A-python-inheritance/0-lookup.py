#!/usr/bin/python3
"""
A module to lookup an object
"""


def lookup(obj):
    """lookup function
    Args:
        obj (any): object to lookup

    Return:
        list of available attributes and methods of an object
    """

    return dir(obj)
