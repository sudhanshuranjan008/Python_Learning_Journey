# ------------------------------------------------------
# File: create_2D_array.py
# Date: 2024-12-28
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Create a 2D array (3x3) where each element is the product of its row and column indices

# Define the dimensions of the 2D array (number of rows and columns)
rows, cols = (5, 5)

# Create a 2D array using list comprehension
# Outer list comprehension iterates over each row
# Inner list comprehension iterates over each column for the current row
# Each element is calculated as the product of the row index (row) and the column index (col)
arr = [[row * col for col in range(cols)] for row in range(rows)]

# Iterate through each row of the 2D array
# Print each row to display the array in a matrix format
for row in arr:
    print(row)
