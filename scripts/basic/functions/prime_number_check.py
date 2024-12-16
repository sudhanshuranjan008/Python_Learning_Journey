# ------------------------------------------------------
# File: prime_number_check.py
# Date: 2024-12-16
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Check if a number is prime

# Prompt the user to input a number to check for primality
num = int(input("Enter the number you want to check as a prime: "))

# Check if the input is less than or equal to 1
# Numbers <= 1 are not prime, and 1 is neither prime nor composite
if num <= 1:
    print("Please enter a positive integer greater than 1. 1 is neither prime nor composite.")
else:
    # Assume the number is prime until proven otherwise
    is_prime = True

    # Loop through potential divisors from 2 to the square root of the number (inclusive)
    for i in range(2, int(num ** 0.5) + 1):
        # Check if the current divisor divides the number without a remainder
        if num % i == 0:
            # If divisible, the number is not prime
            print(f"{num} is not a prime number. {i} is a divisor.")
            is_prime = False  # Set the flag to indicate the number is not prime
            break  # Exit the loop as we found a divisor

    # If the loop completes without finding any divisors, the number is prime
    if is_prime:
        print(f"Yes! {num} is a prime number.")


