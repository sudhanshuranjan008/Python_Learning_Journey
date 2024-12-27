# ------------------------------------------------------
# File: numbers_cube_tuple.py
# Date: 2024-12-26
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Generate a list of tuples where each tuple contains a number and its cube for numbers between 1 and 10

# Generate a list of tuples where each tuple contains a number and its cube
cube_of_number = [(x, x**3) for x in range(1, 11)]  # Directly use range

# Print the list of tuples
print(cube_of_number)  # Output: [(1, 1), (2, 8), (3, 27), (4, 64), (5, 125), (6, 216), (7, 343), (8, 512), (9, 729), (10, 1000)]
