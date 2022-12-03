#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for elements in matrix:
            i = 1
            length = len(elements)

            for e in elements:
                if i == length:
                    print("{:d}".format(e), end='')
                else:
                    print("{:d}".format(e), end='')
                i += 1

            print()
