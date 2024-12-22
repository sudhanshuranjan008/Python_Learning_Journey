# ------------------------------------------------------
# File: diamond_pattern.py
# Date: 2024-12-22
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Print a diamond pattern

# Taking the input from the user to specify the number of rows for one of the halves of the diamond
n = int(input("Enter the number of rows in one of the halves as size: "))

# First loop: creates the top half of the diamond
# The loop starts with 1 star and increases by 2 stars in each iteration, up to (2*n - 1) stars
for i in range(1, 2*n, 2):
    # Printing '*' repeated 'i' times, and centering it within a width of 2*n - 1 for symmetry
    print(("*" * i).center(2*n-1))

# Second loop: creates the bottom half of the diamond
# The loop starts with (2*n - 3) stars and decreases by 2 stars in each iteration, down to 1 star
for j in range(2*n-3, 0, -2):
    # Printing '*' repeated 'j' times, and centering it within a width of 2*n - 1 for symmetry
    print(("*" * j).center(2*n-1))
