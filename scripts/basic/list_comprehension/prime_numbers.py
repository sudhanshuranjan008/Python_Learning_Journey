# ------------------------------------------------------
# File: prime_numbers.py
# Date: 2024-12-26
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Generate a list of prime numbers between 1 and 50 using a single line of list comprehension

prime_numbers = [
    x for x in range(2, 50)  # Iterate through numbers starting from 2 (smallest prime)
    if all(x % y != 0 for y in range(2, int(x**0.5) + 1))  # Check divisibility
    # Explanation of the condition:
    # - range(2, int(x**0.5) + 1): Check divisors from 2 up to sqrt(x).
    # - x % y != 0: Ensure that x is not divisible by any y in this range.
    # - all(): Confirms that x satisfies the condition for all possible divisors.
]

# Print the resulting list of prime numbers
print(prime_numbers)
