#!/usr/bin/python3

"""
Prints all integers of a list, in reversed order
"""
def print_reversed_list_integer(my_list=[]):
    reversed_list = my_list.reverse()

    for i in range(len(reversed_list)):
        print("{:d}".format(reversed_list[i]))
