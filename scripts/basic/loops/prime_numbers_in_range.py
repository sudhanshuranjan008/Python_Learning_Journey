# ------------------------------------------------------
# File: prime_numbers_in_range.py
# Date: 2024-12-20
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find all prime numbers in a given range

import math

# Input the range from the user
min_range = int(input("Enter the minima for the range of numbers: "))
max_range = int(input("Enter the maxima for the range of numbers: "))

# Adjust the minimum range if it's less than 2, as 2 is the smallest prime number
if min_range < 2:
    min_range = 2

# Validate the input range
if max_range < min_range:
    print("Invalid range. 2 is the smallest prime number.")
else:
    prime_numbers = []  # List to store prime numbers

    # Iterate through all numbers in the range
    for i in range(min_range, max_range + 1):
        # Check for factors from 2 to √i
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:  # If divisible, not a prime number
                break
        else:
            prime_numbers.append(i)  # Append prime number to the list

    # Output the result
    if prime_numbers:
        print("The prime numbers in the input range are:", prime_numbers)
    else:
        print("There are no prime numbers in the input range.")
