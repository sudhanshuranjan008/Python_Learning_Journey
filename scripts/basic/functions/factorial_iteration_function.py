# ------------------------------------------------------
# File: factorial_iteration_function.py
# Date: 2024-12-18
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Calculate the factorial of a number using function iteration

# Function to multiply current value by the next number
def multiply(num1, num2):
    return num1 * num2

# Function to calculate factorial using iteration
def factorial(num):
    result = 1  # Start with 1 (factorial base case)
    for i in range(1, num + 1):
        result = multiply(result, i)  # Apply the multiply function iteratively
    return result

# Main program
if __name__ == "__main__":
    var = int(input("Enter a number to calculate its factorial: "))
    if var < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"The factorial of {var} is {factorial(var)}")
