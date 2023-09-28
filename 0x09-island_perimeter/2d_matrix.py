#!/usr/bin/python3

matrix = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 1, 0]
]

# Get the number of rows and columns in the matrix
num_rows = len(matrix)
num_cols = len(matrix[0])
print(num_rows)

# Traverse the matrix using nested loops
for row in range(num_rows):
    # print(row)
    for col in range(num_cols):
        # print(col)
        # Access the current element in the matrix
        current_element = matrix[row][col]
        # print(current_element)
        if current_element == 1:
            print(f"Land found at row {row}, column {col}")
        elif current_element == 0:
            print(f"Water found at row {row}, column {col}")
