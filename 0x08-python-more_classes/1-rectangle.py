#!/usr/bin/python3
"""

This module defines a Rectangle

"""


class Rectangle:
    """

    A Rectangle class

    """


def __init__(self, width=0, height=0):
    """

    Checks the parameters and initializes some values

    Args:
        width (:obj:`int`, optional): The width of the Rectangle.
        height (:obj:`int`, optional): The height of the Rectangle.

    """

    self.width = width
    self.height = height


@property
def width(self):
    """

    Returns the width of the Rectangle

    """

    return self.__width


@width.setter
def width(self, value):
    """

    Checks the parameters and set the size of the Rectangle

    Args:
        value (int): The width of the Rectangle.

    Raises:
        TypeError: If `value` type is not `int`.
        ValueError: If `value` is less than `0`.

    """

    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self.__width = value


@property
def height(self):
    """

    Returns the width of the Rectangle

    """

    return self.__height


@height.setter
def height(self, value):
    """

    Checks the parameters and set the size of the Rectangle

    Args:
        value (int): The height of the Rectangle.

    Raises:
        TypeError: If `value` type is not `int`.
        ValueError: If `value` is less than `0`.

    """
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    self.__height = value
