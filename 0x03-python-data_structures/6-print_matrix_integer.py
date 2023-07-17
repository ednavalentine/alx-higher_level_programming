#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ink in matrix:
        print(" ".join("{:d}".format(number) for number in ink))
