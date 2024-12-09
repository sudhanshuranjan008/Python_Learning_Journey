# ------------------------------------------------------
# File: palindrome_check.py
# Date: 2024-12-01
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Input string and number to check for palindrome

string = " Python "
num = 121

# Normalize the string by removing spaces and converting to lowercase
norm_string = string.replace(" ", "").lower()  # Removes extra spaces and ensures case insensitivity

# Reverse the normalized string using slicing
rev_string = norm_string[::-1]

# Reverse the number by converting it to a string, then reversing
rev_num = str(num)[::-1]

# Check if the normalized string is a palindrome
if norm_string == rev_string:
    print("String is palindrome")
else:
    print("String is not palindrome")

# Check if the number is a palindrome
if num == int(rev_num):  # Convert reversed string back to an integer for comparison
    print("Number is palindrome")
else:
    print("Number is not palindrome")

