# ------------------------------------------------------
# File: math_utils.py
# Date: 2025-01-01
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Create a custom module math_utils with functions for addition, subtraction, and multiplication

# Function to perform addition of two numbers.
def addition(a, b):
    return a + b

# Function to perform subtraction of two numbers.
def subtraction(a, b):
    return a - b

# Function to perform multiplication of two numbers.
def multiplication(a, b):
    return a * b

# If the script is run directly, test the functions with example inputs.
if __name__ == "__main__":
    print("Testing math_utils module")  # Indicate the start of testing.
    # Test the addition function with example inputs.
    print(f"5 + 3 = {addition(5, 3)}")
    # Test the subtraction function with example inputs.
    print(f"5 - 3 = {subtraction(5, 3)}")
    # Test the multiplication function with example inputs.
    print(f"5 * 3 = {multiplication(5, 3)}")


