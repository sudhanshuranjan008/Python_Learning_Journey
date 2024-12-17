# ------------------------------------------------------
# File: variable_arguments_sum.py
# Date: 2024-12-16
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Write a function that accepts variable arguments (*args) and returns their sum

# Function that accepts variable arguments (*args) and returns their sum
def variable_sum(*var):
    # Use Python's built-in sum function to calculate the sum of all arguments
    return sum(var)

# Call the function with multiple arguments
total = variable_sum(23, 56, 79)

# Print the result
print("The sum of values passed as arguments is:", total)

