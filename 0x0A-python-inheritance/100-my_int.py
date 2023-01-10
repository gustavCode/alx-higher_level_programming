#!/usr/bin/python3
"""
A module to modify int class methods
"""


class MyInt(int):
    """
    MyInt class modifies methods of the int class
    """

    def __eq__(self, value):
        """
        Overrides equals method of int class
        """
        self.real != value

    def __ne__(self, value):
        """
        Overrides the not equals method of int class
        """
        self.real == value
