# ------------------------------------------------------
# File: swap_tuples.py
# Date: 2024-12-15
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Write a program to swap two tuples

# Swapping tuples using a temporary variable (traditional method)
num1 = (2, 3, 5, 7)
num2 = (11, 13, 17, 19)
print("\nUsing traditional method with a temporary variable:")
print("Original tuples are: ", num1, '\n', num2)

temp = num1  # Temporary variable to store the first tuple
num1 = num2  # Assign second tuple to the first variable
num2 = temp  # Assign the temporary variable to the second tuple
print("Swapped tuples are: ", num1, '\n', num2)

# Swapping tuples using Python's tuple unpacking (modern method)
fruits = ("Apple", "Orange", "Mango", "Grapes", "Papaya")
flowers = ("Rose", "Lotus", "Hibiscus", "Lilly", "Jasmine")
print("\nUsing Python's tuple unpacking:")
print("Original tuples are: ", fruits, "\n", flowers)

fruits, flowers = flowers, fruits  # Swapping using Python's built-in functionality
print("Swapped tuples are: ", fruits, '\n', flowers)
