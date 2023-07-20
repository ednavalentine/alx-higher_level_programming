#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_mat = []
    for row in matrix:
        square_row = []
        for ink in row:
            square_row.append(ink ** 2)
        square_mat.append(square_row)
    return square_mat
