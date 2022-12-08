#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []

    for x, y in a_dictionary.items():
        if y == value:
            keys.append(x)

    for x in keys:
        del a_dictionarey[x]

    return a_dictionary
