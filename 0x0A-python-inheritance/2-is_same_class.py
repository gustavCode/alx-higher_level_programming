#!/usr/bin/python3
"""
A module to compare obj and a_class
"""


def is_same_class(obj, a_class):
    """
    Checks if `0bj` is exactly an instance of a specified class

    Args:
        obj (any): object to compare
        a_class (any): class to compare with the object

    Returns:
        `True` if the object is exactly an instannce of class
        otherwise `False`
    """

    if type(obj) == a_class:
        return True

    return False
