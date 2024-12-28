# ------------------------------------------------------
# File: 2D_array_rotation.py
# Date: 2024-12-28
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Rotate a given 2D array (matrix) 90 degrees clockwise

rows, cols = 3, 3  # Define the number of rows and columns for the matrix

# Initialize and assign values to the matrix
arr = [[0 for row in range(rows)] for col in range(cols)]  
# This creates a 3x3 matrix with all elements initialized to 0.
# Note: This uses a list comprehension to generate rows, where each row is a list of zeros.

arr[0][0] = 45  # Assign 45 to the element at position (0, 0)
arr[2][2] = 55  # Assign 55 to the element at position (2, 2)
arr[0][2] = 13  # Assign 13 to the element at position (0, 2)
arr[2][0] = 67  # Assign 67 to the element at position (2, 0)

# Initialize the rotated matrix
rotated_arr = [[None for row in range(rows)] for col in range(cols)]  
# This creates a new 3x3 matrix with all elements initialized to None.
# We will use this matrix to store the rotated version of the original matrix.

# Perform 90° clockwise rotation
for row in range(rows):  # Iterate through each row of the original matrix
    for col in range(cols):  # Iterate through each column of the original matrix
        # The element from position (row, col) in the original matrix is placed in the new position
        rotated_arr[col][rows - 1 - row] = arr[row][col]
        # Explanation of index placement:
        # The row becomes the column in the rotated matrix.
        # The column index becomes the new row index in the rotated matrix.
        # `rows - 1 - row` adjusts the row index for the rotated position (flips the rows top-down).

# Print the original matrix
print("The original matrix is as below:")
for row in arr:  # Iterate through each row in the original matrix and print it
    print(row)

# Print the rotated matrix
print("The rotated matrix is as below:")
for row in rotated_arr:  # Iterate through each row in the rotated matrix and print it
    print(row)

