#!/usr/bin/python3
"""
A module that insersts a line
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each
    line containing a specific string

    Args:
        filename : text file
        search_string : specific string
        new_string : new string to insert
    """

    with open(filename, mode='r', encoding='utf-8') as f:
        text = f.readlines()
        new_text = []

        for line in text:
            new_text.append(line)

            if search_string in line:
                new_text.append(new_string)

    with open(filename, mode='w', encoding='utf-8') as nf:
        for line in new_text:
            nf.write(line)
