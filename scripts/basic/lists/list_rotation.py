# ------------------------------------------------------
# File: list_rotation.py
# Date: 2024-12-03
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Rotate a list by k elements (e.g., [1,2,3,4,5] rotated by 2 becomes [4,5,1,2,3]).

# Define the original list
mylist = [18,27,3,4,16,9]

# Set the number of positions to rotate
k = 2

# Ensure k is within the range of the list length using modulo operation
# This handles cases where k is larger than the length of the list
k = k % len(mylist)

# Use slicing to rotate the list:
# - mylist[-k:] takes the last 'k' elements
# - mylist[:-k] takes the remaining elements
rotated_list = mylist[-k:] + mylist[:-k]

# Print the original list
print("Original list is: ", mylist)

# Print the rotated list
print("The rotated list is: ", rotated_list)
