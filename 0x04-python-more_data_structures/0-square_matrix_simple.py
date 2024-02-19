#!/usr/bin/python3


"""function that computes the square value of all integers of a matrix"""


def square_matrix_simple(matrix=[]):
    res = []
    for i in matrix:
        res.append(list(map(lambda x: x * x, i)))
    return res
