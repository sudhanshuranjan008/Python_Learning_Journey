# ------------------------------------------------------
# File: right_angled_triangle_flipped_pattern.py
# Date: 2024-12-22
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Print a flipped right-angled triangle pattern of stars (*) 

# Take input from the user for the number of rows in the pattern
n = int(input("Enter the number of rows as size: "))

# Outer loop to control the number of rows
for i in range(1, n+1):
    # Inner loop to print spaces for the right alignment
    for j in range(n, i, -1):
        print(" ", end="")  # Print space without a newline
    
    # Inner loop to print '*' for each column in the current row
    for k in range(1, i+1):
        print("*", end="")  # Print '*' without a newline
    
    # Move to the next line after printing spaces and stars in the current row
    print()

