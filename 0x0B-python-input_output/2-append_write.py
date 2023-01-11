#!/usr/bin/python3
"""
A module to append a string to end of a file
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file

    Args:
        filename (str): file to append to
        text (str): string to append to file

    Returns:
        number of characters added
    """

    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
