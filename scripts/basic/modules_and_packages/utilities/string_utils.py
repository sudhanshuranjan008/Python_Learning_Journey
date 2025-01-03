# ------------------------------------------------------
# File: string_utils.py
# Date: 2025-01-03
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Writa a function to count vowels in a string

# Function to count vowels in a string
def vowel_count(mystring):
    # Initialize count to 0
    count = 0
    
    # Loop through each character in the string
    for ch in mystring:
        # Check if the character is a vowel (case-insensitive)
        if ch.lower() in ("a", "e", "i", "o", "u"):
            count += 1  # Increment the count if it's a vowel
    
    # Return the total count of vowels
    return count
