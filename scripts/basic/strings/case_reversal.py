# ------------------------------------------------------
# File: case_reversal.py
# Date: 2024-12-01
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Convert a string to uppercase and lowercase without using built-in functions
string = "Python-Learning-Journey"  # Input string
case_string = ""  # Initialize an empty string to store converted characters

# Loop through each character in the string
for ch in string:
    ascii_value = ord(ch)  # Get the ASCII value of the character
    
    # Check if the character is a lowercase letter (ASCII range: 97-122)
    if 97 <= ascii_value <= 122:  
        case_string += chr(ascii_value - 32)  # Convert to uppercase by subtracting 32 from ASCII value
    # Check if the character is an uppercase letter (ASCII range: 65-90)
    elif 65 <= ascii_value <= 90:  
        case_string += chr(ascii_value + 32)  # Convert to lowercase by adding 32 to ASCII value
    else:
        case_string += ch  # Keep non-alphabetic characters unchanged

# Print the original string
print("Original String:", string)

# Print the transformed string with swapped cases
print("Transformed String:", case_string)
