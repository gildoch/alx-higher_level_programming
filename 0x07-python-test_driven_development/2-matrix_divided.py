#!/usr/bin/python3
"""
This is the "matrix_divided" module
The 2-matrix_divided module supplies one function, matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """ Function to divid a matrix by a number
    Args:
        matrix (list): matrix to perfom the divisio
        div (int): number do divid each matrix element
    Returns:
        new matrix with divided numbers
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    lenght = None
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        if lenght is None:
            lenght = len(row)
        elif lenght != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    divided_matrix = []
    for row in matrix:
        divided_matrix.append([round(elem / div, 2) for elem in row])
    return divided_matrix
