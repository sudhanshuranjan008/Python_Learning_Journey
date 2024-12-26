# ------------------------------------------------------
# File: value_error.py
# Date: 2024-12-25
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Write a program to handle the value error exceptions

try:
    # Prompt the user to enter a number and convert it to an integer
    num = int(input("Enter a number to find its square: "))
    
    # Calculate and print the square of the entered number
    print(f"The square of {num} is ", num ** 2)

# Handle ValueError if the user enters a non-integer value
except ValueError:
    print("Invalid input. Please enter a valid integer.")
