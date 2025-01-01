# ------------------------------------------------------
# File: math_operations.py
# Date: 2025-01-01
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Import math_utils module and perform arithmetic operations

import math_utils as mu

try:
    # Prompt the user for two integer inputs
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Display results of arithmetic operations
    print("\nBasic arithmetic operations on the numbers:")
    print(f"{num1} + {num2} = {mu.addition(num1, num2)}")
    print(f"{num1} - {num2} = {mu.subtraction(num1, num2)}")
    print(f"{num1} × {num2} = {mu.multiplication(num1, num2)}")

except ValueError:
    # Handle cases where the input is not a valid integer
    print("\nInvalid input. Please enter valid integers.")

finally:
    # Always display a completion message
    print("\nActivity completed!")

