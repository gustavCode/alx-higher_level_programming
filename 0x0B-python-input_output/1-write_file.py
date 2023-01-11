#!/usr/bin/python3
"""
A module to write a string to a file
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file

    Args:
        filename (str): text file to write to
        text (str): string to write to the file

    Returns:
        number of characters written
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
