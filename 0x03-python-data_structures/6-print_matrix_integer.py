#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for number in rows:
            print("{:d}".format(number), end=" ")
        print()
