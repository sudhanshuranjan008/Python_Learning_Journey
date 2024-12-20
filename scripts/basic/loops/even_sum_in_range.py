# ------------------------------------------------------
# File: even_sum_in_range.py
# Date: 2024-12-20
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Sum of all even numbers in a range

# Input range from the user
min_range = int(input("Enter the minima for the range of numbers: "))
max_range = int(input("Enter the maxima for the range of numbers: "))

# If the minimum range is odd, start from the next even number
if min_range % 2 != 0:
    min_range += 1

# Initialize total sum and iterate through even numbers in the range
total = 0
for num in range(min_range, max_range + 1, 2):  # Step of 2 ensures we only check even numbers
    total += num

# Output the result
print(f"The sum of even numbers in the range is: {total}")
