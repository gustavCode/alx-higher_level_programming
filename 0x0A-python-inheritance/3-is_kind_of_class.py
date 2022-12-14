#!/usr/bin/python3
"""
A module that checks if an object inherits from a_class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if `obj` is the same class or inherits from `a_class`

    Args:
        obj (any): object to compare
        a_class (any): class to compare with the object

    Returns:
        `True` if the object inherits from specified class
        otherwise `False`
    """

    return isinstance(obj, a_class)
