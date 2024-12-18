# ------------------------------------------------------
# File: prime_check_function.py
# Date: 2024-12-18
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Create a function to check if a number is prime

# Import the math module for efficient square root calculations
import math

# Define a function to check if a number is prime
def prime_check(num):
    # Check if the number is less than or equal to 1
    if num <= 1:
        # Inform the user that prime numbers start from 2
        print("Please enter a number greater than 1.")
        print("2 is the smallest prime!")
    else:
        # Loop from 2 to the square root of the number
        for i in range(2, int(math.sqrt(num)) + 1):
            # Check if the number is divisible by the current value of i
            if num % i == 0:
                # If divisible, it is not a prime number
                print(f"{num} is not a prime number.")
                break
        else:
            # If the loop completes without finding a divisor, it is a prime number
            print(f"{num} is a prime number.")

# Main block of the program to get user input and call the function
if __name__ == "__main__":
    # Prompt the user for input
    P = int(input("Enter a number to check if it is prime or not: "))
    # Call the function with the user-provided number
    prime_check(P)
