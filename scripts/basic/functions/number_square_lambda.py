# ------------------------------------------------------
# File: number_square_lambda.py
# Date: 2024-12-16
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Write a lambda function to calculate the square of a number

# Ask the user to input a number, ensuring it is an integer for squaring
num = int(input("Enter a number to find its square: ")) 

# Lambda function to calculate the square of the input number
num_square = lambda num : num ** 2

# Output the result using an f-string for clear formatting
print(f"The square of number {num} is {num_square(num)}")
