#!/usr/bin/python3

"""Contains a function that rotates a matrix 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """
    Rotate 2d matrix
    Args:
        matrix:
        matrix
    Returns:
        Rotated matrix
    """

    duplicated_matrix = [row[:] for row in matrix]
    matrix_size = len(matrix)
    print(matrix_size)
    b = -1
    # iterate through each row in the duplicated matrix
    for row in duplicated_matrix:
        # Iterate through each column in the original matrix
        for a in range(matrix_size):
            # update the values of the original matrix with the values
            # from the copied matrix
            matrix[a][b] = row[a]
        # Move to the previous column for the next iteration
        b -= 1
