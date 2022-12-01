#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """
    Prints the number of and list of arguments
    """

    ar = sys.argv
    len_argv = len(ar) - 1

    if len_argv > 1:
        print(len_argv, "arguments:")
        for i in range(1, len_argv + 1):
            print("{:d} {}".format(i, ar[i]))
    elif len_argv == 1:
        print(len_argv, "argument:")
        for i in range(1, len_argv + 1):
            print("{:d} {}".format(i, ar[i]))
    elif len_argv == 0:
        print(len_argv, "arguments.")
