#!/usr/bin/python3
"""
A module to inherit from a base class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A square class that inherits from BaseGeometry class
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
