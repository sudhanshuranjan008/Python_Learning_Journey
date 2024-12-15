# ------------------------------------------------------
# File: create_even_number_tuple.py
# Date: 2024-12-15
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Create a tuple containing only even numbers from a given tuple

mytuple = (81, 63, 94, 76, 42, 1, 3, 7, 8)
even_list = []
for x in mytuple:
    even_list.append(x) if x % 2 == 0 else None  # Conditional expression for adding even numbers to the list

# Convert the list of even numbers into a tuple
even_tuple = tuple(even_list)
print(even_tuple)


# Using tuple comprehension for a more concise solution

num = (23, 56, 45, 15, 12, 14, 17, 15, 19, 61, 43)
# Create a new tuple directly with even numbers from the original tuple using comprehension
even_num = tuple(x for x in num if x % 2 == 0)
print(even_num)

