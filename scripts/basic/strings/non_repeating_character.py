# ------------------------------------------------------
# File: non_repeating_character.py
# Date: 2024-12-01
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Given string to find the first non-repeating character
string = "pythonproblem"

# Loop through each character in the string
for i in range(0, len(string)):
    # Flag to track if the current character repeats in the string
    found = False

    # Inner loop to compare the current character with every other character in the string
    for j in range(0, len(string)):
        # If a matching character is found (but not the same index), mark as repeated
        if (i != j and string[i] == string[j]):
            found = True
            break  # No need to continue checking if a match is found

    # If no match is found, the character is non-repeating
    if not found:
        # Print the first non-repeating character and break the loop
        print("The first non-repeating character is:", string[i])
        break  # Exit the loop after finding the first non-repeating character

