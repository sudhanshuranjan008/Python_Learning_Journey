# ------------------------------------------------------
# File: remove_duplicates.py
# Date: 2024-12-02
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Remove duplicates from a list using a loop

# Original list with duplicates
num = [12, 54, 12, 87, 54, 98, 99, 87]

# Create a new list to store unique values
# Efficiency: O(n^2) in the worst case because for each element in `num`,
# we are checking if it exists in `new_num` (which involves a linear search).
new_num = []
for val in num:
    # Check if the value is not already in the new list
    if val not in new_num:
        # Add the value to the new list
        new_num.append(val)

# Print the original list (unchanged)
print("The original num list is: ", num)
# Print the new list with duplicates removed
print("The new num list without duplicate values is: ", new_num)

# Another way: Using a set to remove duplicates

# Original list with duplicates
score = [11, 33, 22, 24, 33, 11, 67, 34, 22]

# Use set to remove duplicates and convert it back to a list
# Efficiency: O(n) on average because adding elements to a set
# and iterating through it are constant time operations for each element.
new_score = list(set(score))

# Print the original list (unchanged)
print("The original score list is: ", score)
# Print the new list with duplicates removed
print("The new score list without duplicate values is: ", new_score)
