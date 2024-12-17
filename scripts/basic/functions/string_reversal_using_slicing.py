# ------------------------------------------------------
# File: string_reversal_using_slicing.py
# Date: 2024-12-16
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Create a function to reverse a string using slicing

# Function to reverse a string using slicing
def string_reversal(get_str):
    # Slicing to reverse the string (::-1 reverses the string)
    return get_str[::-1]

# Define the original string
mystring = "PythonFunction"

# Call the function to reverse the string
reversed_string = string_reversal(mystring)

# Print the original string
print("Original string is:", mystring)

# Print the reversed string
print("Reversed string is:", reversed_string)
