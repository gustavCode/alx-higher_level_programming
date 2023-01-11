#!/usr/bin/python3
"""
Class to JSON
"""


def class_to_json(obj):
    """
    Returns dictionary description with simple
    data structure for JSON serialization

    Args:
        obj (any): instance of a class

    Returns:
        dictionary description
    """

    return obj.__dict__
