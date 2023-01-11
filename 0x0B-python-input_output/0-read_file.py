#!/usr/bin/python3
"""
A module to read and print a text file to stdout
"""


def read_file(filename=""):
    """
    Reads a text file and prints to stdout

    Args:
        filename (str): text file to read
    """

    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
