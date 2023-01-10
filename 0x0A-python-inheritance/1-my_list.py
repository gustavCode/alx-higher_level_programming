#!/usr/bin/python3
"""
A module to print a sorted list in ascending order
"""


class MyList(list):
    """
    A class that inherits from list class
    """

    def print_sorted(self):
        """
        Prints sorted list in ascending order
        """

        if issubclass(MyList, list):
            print(sorted(self))
