#!/usr/bin/python3
"""
A module to add attributes to an object if possible
"""


def add_attribute(obj, attr_variable, attr_value):
    """
    Adds an attribute to an object

    Args:
        obj (any): object to add attribute to
        attr_variable (any): attribute variable name
        attr_value (any): attribute value

    Raises:
        TypeError: if the object can’t have new attribute
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_variable, attr_value)
