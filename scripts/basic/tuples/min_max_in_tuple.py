# ------------------------------------------------------
# File: min_max_in_tuple.py
# Date: 2024-12-13
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find the largest and smallest elements in a tuple

# Using loop method
mytuple = (45, 26, 13, 58, 65, 85, 99)

# Initialize min and max with the first element of the tuple
min_val = mytuple[0]
max_val = mytuple[0]

# Iterate through the tuple to find the min and max elements
for i in mytuple:
    if i > max_val:  # Update max if a larger element is found
        max_val = i
    elif i < min_val:  # Update min if a smaller element is found
        min_val = i

# Print the results
print(f"The smallest element in mytuple is: {min_val}; and the largest element is: {max_val}")


# Using list sorting method

prime = (13, 17, 19, 2, 5, 3, 7, 11)

# Sort the tuple and convert it back to a tuple
sorted_prime = tuple(sorted(prime))

# Access the first and last elements as the smallest and largest
print(f"The smallest element in the prime tuple is: {sorted_prime[0]}; and the largest is: {sorted_prime[-1]}")


# Using built-in function (optimized)

# Find the largest and smallest elements in a tuple using built-in functions
mytuple = (45, 26, 13, 58, 65, 85, 99)
print(f"The smallest element in mytuple is: {min(mytuple)}; and the largest element is: {max(mytuple)}")

# Using built-in functions for another tuple
prime = (13, 17, 19, 2, 5, 3, 7, 11)
print(f"The smallest element in the prime tuple is: {min(prime)}; and the largest is: {max(prime)}")
