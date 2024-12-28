# ------------------------------------------------------
# File: element_sum.py
# Date: 2024-12-27
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Write a program to find the sum of all elements in an array

from array import array

# Define the array
num_array = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])  # 'i' stands for integers

# Initialize total
total = 0

# Calculate the sum using a loop
for num in num_array:
    total += num

# Print the result
print(f"The sum of all elements in the array is: {total}")

