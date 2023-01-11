#!/usr/bin/python3
"""
Pascal's triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing Pascal's triange of n

    Args:
        n (int): size of triangle

    Returns:
        a list of lists of integers
        otherwise empty list if n <= 0
    """

    if n <= 0:
        return []

    limit = n - 1
    triangle = [[1]]

    for i in range(limit):
        row = []
        row.append(1)

        if len(triangle[i]) > 1:
            prev_row_len = len(triangle[i]) - 1
            nxt = 1

            for j in range(prev_row_len):
                suma = triangle[i][j] + triangle[i][nxt]
                row.append(suma)
                nxt += 1

        row.append(1)
        triangle.append(row)

    return triangle
