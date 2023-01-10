#!/usr/bin/python3
"""
A base geometry module that validates integers
"""


class BaseGeometry:
    """
    A BaseGeometry class that raises an exception
    and validates integer types
    """

    def area(self):
        """
        Raises an exception when called
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates an integer value

        Args:
            name (str): name of the value
            value (int): integer value

        Raises:
            TypeError: if `value` is not an integer
            ValueError: if `value` is <= 0
        """

        if type(value) is not int:
            raise TypeError(name + ' must be an integer')

        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
