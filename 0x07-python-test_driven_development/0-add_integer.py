#!/usr/bin/python3
"""A module to add two numbers

This module adds two numbers together and these
numbers must be integers or float

"""

def add_integer(a, b=98):
    """Add two integers

    Performs the addition of two numbers

    Args:
        a (:obj:`int`, `float`): First number
        b (:obj:`int`, `float`, optional): Second number

    Returns:
        int: result of addition

    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    a = cast_to_int(a)
    b = cast_to_int(b)


def cast_to_int(number):
    """Cast type of number

    Cast the type of number from float to int

    Args:
        number (:obj:`int`, `float`): number to cast

    Returns:
        int: number casted to integer

    """
    if type(number) is float:
        number = int(number)
        return number

    return number
