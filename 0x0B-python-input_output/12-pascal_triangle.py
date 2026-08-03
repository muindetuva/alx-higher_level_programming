#!/usr/bin/python3
"""Build Pascal's triangle without importing modules."""


def pascal_triangle(n):
    """Return a list containing the first n rows of Pascal's triangle."""
    if n <= 0:
        return []

    triangle = []
    for row_index in range(n):
        row = [1] * (row_index + 1)
        for column in range(1, row_index):
            row[column] = (
                triangle[row_index - 1][column - 1]
                + triangle[row_index - 1][column]
            )
        triangle.append(row)
    return triangle
