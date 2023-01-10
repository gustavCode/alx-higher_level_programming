#!/usr/bin/python3
"""
A base geometry module
"""


class BaseGeometry:
    """
    A BaseGeometry class that raises an exception
    """

    def area(self):
        """
        Raises an exception when called
        """

        raise Exception('area() is not implemented')
