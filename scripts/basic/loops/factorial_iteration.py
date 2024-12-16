# ------------------------------------------------------
# File: factorial_iteration.py
# Date: 2024-12-16
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Calculate the factorial of a number using iteration

try:
    # Prompt the user for input and attempt to convert it to an integer
    num = int(input("Enter the number of which you want to calculate factorial: "))
except ValueError:
    # Handle cases where the input is not a valid integer
    print("Please enter a valid number, i.e. a non-negative integer")
else:
    # Check if the input is non-negative
    if num >= 0:
        # Initialize factorial variable before starting the loop
        factorial = 1  # Initialize to 1 since 0! = 1 by definition
        # Using loop, iterate till the input number
        for i in range(1, num + 1):  # Start from 1 to avoid multiplying by 0
            factorial *= i
        # Print the result after the loop completes
        print(f"The factorial of number {num} is {factorial}")
    else:
        # Inform the user that factorial is not defined for negative numbers
        print("Factorial for negative integers is not defined.")
