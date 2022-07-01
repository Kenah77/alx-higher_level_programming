#!/usr/bin/python3
# 14-pascal_triangle.py
"""Defines Pascal's Triangle func.
"""


def pascal_triangle(n):
    """Represent triandle of size n.

    Returns list of lists of int rep the triangle.
    """
    if n <= 0:
        return []

    tris = [[1]]
    while len(tris) != n:
        tri = tris[-1]
        length = [1]
        for i in range(len(tri) - 1):
            length.append(tri[i] + tri[i + 1])
        length.append(1)
        tris.append(length)
    return tris
