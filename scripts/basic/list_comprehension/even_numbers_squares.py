# ------------------------------------------------------
# File: even_numbers_squares.py
# Date: 2024-12-26
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Create a list of squares for all even numbers from 1 to 20

square_list = [x**2 for x in range(1, 21) if x % 2 == 0]  # List comprehension to square even numbers
print(square_list)  # Print the list of squares