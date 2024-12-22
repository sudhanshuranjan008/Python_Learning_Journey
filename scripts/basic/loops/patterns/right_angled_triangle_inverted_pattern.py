# ------------------------------------------------------
# File: right_angled_triangle_inverted_pattern.py
# Date: 2024-12-22
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Print a inverted right-angled triangle pattern of stars (*) 

# Take input from the user for the number of rows in the pattern
n = int(input("Enter the number of rows as size: "))

# Outer loop to control the number of rows (decreasing from n to 1)
for i in range(n, 0, -1):
    # Inner loop to print '*' for each column in the current row
    for j in range(i, 0, -1):
        print("*", end="")  # Print '*' without a newline
    
    # Move to the next line after printing all '*' in the current row
    print()
