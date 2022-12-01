#!/usr/bin/python3
import sys

if __name__ = "__main__":
    """
    Prints the results of the addition of all arguments
    """

    ar = sys.argv
    l_arg = len(ar)
    sum_arg = 0

    if l_arg > 1:
        for i in range(1, l_arg):
            sum += int(ar[i])

    print(sum_arg)
