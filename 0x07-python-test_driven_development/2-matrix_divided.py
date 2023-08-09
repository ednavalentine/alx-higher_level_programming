#!/usr/bin/python3
"""Divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Check to see if the matrix is a int or float"""
    valid_matrix = all(isinstance(row, list) for row in matrix) and all(
            isinstance(val, (int, float)) for row in matrix for val in row)
    if not valid_matrix:
        raise TypeError("matrix must be a matrix \
                (list of lists) of integers/floats")
    """Checks if each rows have the same size in the matrix"""
    length_rows = set(len(row) for row in matrix)
    if len(length_rows) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    """Checks if div is a number and not equal to 0"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    """Checking the division and rounding of the matrix"""
    matrix_res = []
    for row in matrix:
        row_res = [round(val / div, 2) for val in row]
        matrix_res.append(row_res)
    return matrix_res
