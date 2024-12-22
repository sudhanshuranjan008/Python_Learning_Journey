# ------------------------------------------------------
# File: pyramid_pattern.py
# Date: 2024-12-22
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Print a pyramid pattern using nested loops

n = int(input("Enter the number of rows as size: "))

# Outer loop for the number of rows
for i in range(1, n + 1):  # 'i' ranges from 1 to 'n' (inclusive)
    
    # Inner loop for spaces before the stars
    for j in range(n - i):  # Number of spaces decreases as 'i' increases
        print(" ", end="")  # Print spaces without moving to the next line

    # Inner loop for stars in each row
    for k in range(2 * i - 1):  # Number of stars increases as 'i' increases
        print("*", end="")  # Print stars without moving to the next line

    # Move to the next line after printing all spaces and stars for a row
    print()