# ------------------------------------------------------
# File: nested_list_flatten.py
# Date: 2024-12-26
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Flatten a nested list [[1, 2], [3, 4], [5, 6]] using list comprehension

nested_num = [[1, 2], [3, 4], [5, 6]]

# Flattening the nested list using list comprehension
flattened_num = [flat_num for num in nested_num for flat_num in num]

# Output the flattened list
print(flattened_num)  # Output: [1, 2, 3, 4, 5, 6]
