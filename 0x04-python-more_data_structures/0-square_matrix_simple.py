#!/usr/bin/python3
# 0-square_matrix_simple.py


def square_matrix_simple(matrix=[]):
    """Compute square of all int elements in a matrix."""
    return ([[col * col for col in row] for row in matrix])
