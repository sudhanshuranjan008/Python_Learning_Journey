# ------------------------------------------------------
# File: multiplication_table.py
# Date: 2024-12-20
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Program to create a multiplication table for a given number

# Prompt the user to enter a number for which the multiplication table is needed
num = int(input("Please enter any number to get its multiplication table: "))

# Display the title of the table with the number provided
print(f"Table of {num} is as below:")

# Loop from 1 to 10 to calculate and display the multiplication table
for i in range(1, 11):  # Iterates through the numbers 1 to 10
    # This ensures neat alignment for all numbers, regardless of their length.
    print(f"{num:>3} x {i:>2} = {num * i:>4}")
