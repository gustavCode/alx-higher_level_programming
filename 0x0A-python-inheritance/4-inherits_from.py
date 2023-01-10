#!/usr/bin/python3
"""
A module to check if an object is an instance of a class
"""


def inherits_from(obj, a_class):
    """
    Checks if `obj` is an instance of a class
    that inherits from `a_class`

    Args:
        obj (any): object to compare
        a_class (any): class to compare with the object

    Returns:
        `True` if the object is an instance of a class that
        inherited (directly or indirectly) from the
        specified class ; otherwise `False`
    """

    if isinstance(obj, a_class) and \
            issubclass(a_class, obj.__class__) is False:
                return True

    return False
