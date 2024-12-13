# ------------------------------------------------------
# File: square_dictionary.py
# Date: 2024-12-10
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Create a dictionary where keys are numbers (1–10) and values are their squares.

# Using a loop
dict_square = {}  # Initialize an empty dictionary
for i in range(1, 11):  # Iterate through numbers 1 to 10
    dict_square[i] = i * i  # Add the key-value pair to the dictionary

print("The square dictionary using a loop is:", dict_square)

# Using dictionary comprehension (simpler method)
dict_square_comp = {i: i * i for i in range(1, 11)}
print("The square dictionary using dictionary comprehension is:", dict_square_comp)
