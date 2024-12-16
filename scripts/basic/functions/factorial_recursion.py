# ------------------------------------------------------
# File: factorial_recursion.py
# Date: 2024-12-15
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Calculate the factorial of a number using recursion

# Function to calculate the factorial of a number using recursion
def factorial(x):
    # Base case: the factorial of 0 is defined as 1
    if x == 0:
        return 1   
    # Recursive case: x multiplied by the factorial of (x-1)
    return x * factorial(x-1)


# Ensures that this block runs only if the script is executed directly
if __name__ == "__main__":
    try:
        # Prompt the user for input and attempt to convert it to an integer
        num = int(input("Enter the number of which you want to calculate factorial: "))
    except ValueError:
        # Handle cases where the input is not a valid integer
        print("Please enter a valid number, i.e. a non-negative integer")
    else:
        # Check if the input is non-negative
        if num >= 0:
            # Call the factorial function and print the result
            result = factorial(num)
            print(f"The factorial of number {num} is {result}")
        else:
            # Inform the user that factorial is not defined for negative numbers
            print("Factorial for negative integers is not defined.")

        
   
    