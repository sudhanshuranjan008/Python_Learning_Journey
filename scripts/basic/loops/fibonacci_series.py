# ------------------------------------------------------
# File: fibonacci_series.py
# Date: 2024-12-19
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Print fibonacci series up to n terms

# Take user input for the number of terms in the Fibonacci series
n = int(input("Enter the number of terms for Fibonacci series: "))

# Check for invalid input (negative or zero)
if n <= 0:
    print("Incorrect input. Please enter a positive number.")
else:
    # Initialize the first two terms of the Fibonacci sequence
    a, b = 0, 1
    
    # Loop to print the Fibonacci sequence up to n terms
    for _ in range(n):
        # Print the current term (a) followed by a space
        print(a, end=" ")
        
        # Update the values of a and b for the next term
        a, b = b, a + b  # a gets the value of b, and b gets the sum of a and b

