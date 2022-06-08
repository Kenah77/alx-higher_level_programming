#!/usr/bin/python3
"""Defines matrix divide func
"""


def matrix_divided(matrix, div):
    """Divide every element of a matrix by div
    """
    if div != int(div) or div != float(div)
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Every row of the matrix must be of same size")
    if not all(type(num) in [int, float] for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    lat_matrix = [[eval("{:.2f}".format(num / div)) for num in row]
                  for row in matrix]
    return lat_matrix
