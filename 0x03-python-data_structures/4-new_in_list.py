#!/usr/bin/python3

"""
Replaces an element in a list at a specific
position without modifying the original list
"""
def new_in_list(my_list, idx, element):
    copy_list = my_list

    if (idx < 0):
        return copy_list
    elif (idx > len(copy_list)):
        return copy_list
    else:
        copy_list[idx] = element
        return copy_list
