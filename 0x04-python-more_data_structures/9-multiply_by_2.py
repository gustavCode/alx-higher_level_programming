#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy_dictionary = a_dictionary.copy()

    for x, y in copy_dictionary.items():
        copy_dictionary[x] = y * 2

    return copy_dictionary
