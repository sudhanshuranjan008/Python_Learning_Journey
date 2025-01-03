# ------------------------------------------------------
# File: using_utilities_module.py
# Date: 2025-01-03
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Program to check for an even number and count vowels in a string using the utilities module

# Import the utilities package and its submodules
import utilities.number_utils  # Submodule for number-related functions
import utilities.string_utils  # Submodule for string-related functions

# Prompt the user to enter a number and check if it's even
num = int(input("Please enter a number to check if it is even or not: "))
if utilities.number_utils.iseven(num):  # Call the iseven function from number_utils
    print(f"{num} is an even number.")
else:
    print(f"{num} is not an even number.")

# Prompt the user to enter a string and count the vowels
a_string = input("Please enter a sentence to check the number of vowels in it: ")
count = utilities.string_utils.vowel_count(a_string)  # Call the vowel_count function from string_utils
print(f"Number of vowels in '{a_string}' are: {count}")
