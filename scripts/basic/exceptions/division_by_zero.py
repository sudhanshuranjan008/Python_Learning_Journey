# ------------------------------------------------------
# File: division_by_zero.py
# Date: 2024-12-25
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Write a program to handle the division by zero exceptions

# Prompt the user to enter the numerator and convert the input to an integer
num = int(input("Enter the numerator: "))

# Prompt the user to enter the denominator and convert the input to an integer
den = int(input("Enter the denominator: "))

try:
    # Attempt to divide the numerator by the denominator and print the result
    print("The division is equal to:", num / den)

# Handle the case where the denominator is zero
except ZeroDivisionError:
    print("Division by zero is not defined. Please enter a non-zero denominator.")

# Handle the case where the input cannot be converted to an integer
except ValueError:
    print("Invalid input. Please enter integers only.")
