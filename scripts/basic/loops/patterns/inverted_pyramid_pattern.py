# ------------------------------------------------------
# File: inverted_pyramid_pattern.py
# Date: 2024-12-22
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Print a inverted pyramid pattern

# Take input from the user for the number of rows in the pattern
n = int(input("Enter the number of rows as size: "))

# Outer loop to control the number of rows (start from 2n-1 and decrease by 2)
for i in range(2*n-1, 0, -2):
    # Print '*' repeated i times and center-align it in a field of width (2n-1)
    print(("*" * i).center(2*n - 1))  # Center the stars within a width of (2n-1)
