# ------------------------------------------------------
# File: word_position_search.py
# Date: 2024-12-24
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find the position of a word in a file

# Open the file in read mode and read all lines
with open("practice.txt", "r") as input_file:
    lines = input_file.readlines()  # Reads all lines into a list

# Word to search for
word_to_find = "python"
found = False  # Boolean flag to indicate if the word is found
line_number = 1  # Start line count at 1

# Iterate through each line in the file
for line in lines:
    words = line.split()  # Split the line into a list of words
    if word_to_find in words:  # Check if the word exists in the current line
        position_in_line = words.index(word_to_find) + 1  # Get the 1-based position of the word
        print(f"Word '{word_to_find}' found on line {line_number}, position {position_in_line}")
        found = True  # Set flag to True as the word is found
        break  # Exit the loop once the word is found
    line_number += 1  # Increment line number for the next iteration

# If the word is not found, print a message
if not found:      
    print(f"Word '{word_to_find}' not found in the file.")
