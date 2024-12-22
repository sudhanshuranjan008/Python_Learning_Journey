# ------------------------------------------------------
# File: hourglass_pattern.py
# Date: 2024-12-22
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Print a hourglass pattern

# Taking the input from the user to specify the size for one of the halves
n = int(input("Enter the number of rows in one of the halves as size: "))

# First loop: creates the top half of the pattern (hourglass top)
# This loop decreases the number of stars starting from 2*n - 1, down to 1, with step -2
for i in range(2*n-1, 0, -2):
    # Printing '*' repeated 'i' times, and centering it with width of 2*n-1
    print(("*" * i).center(2*n-1))

# Second loop: creates the bottom half of the pattern (hourglass bottom)
# This loop increases the number of stars starting from 3, up to 2*n - 1, with step +2
for j in range(3, 2*n, 2):
    # Printing '*' repeated 'j' times, and centering it with width of 2*n-1
    print(("*" * j).center(2*n-1))
