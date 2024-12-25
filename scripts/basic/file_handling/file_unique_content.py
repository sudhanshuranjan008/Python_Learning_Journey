# ------------------------------------------------------
# File: file_unique_content.py
# Date: 2024-12-25
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Write a program to create a new file with only unique lines from an existing file

# Open the file 'repeat.txt' in read mode and read all lines
with open("repeat.txt", "r") as input_file:
    lines = input_file.readlines()

# Initialize an empty set to keep track of unique normalized lines
unique_lines = set()

# Open 'unique.txt' in write mode to store unique lines
with open("unique.txt", "w") as new_file:
    for line in lines:
        # Normalize the line by converting to lowercase and removing extraspaces and punctuation
        normalized_line = line.lower().strip().replace(".", "").replace("!", "")
        
        # Check if the normalized line is not in the set
        if normalized_line not in unique_lines:
            new_file.write(line)  # Write the original line to the new file
            unique_lines.add(normalized_line)  # Add the normalized line to the set

# Open 'unique.txt' again in read mode to display its contents
with open("unique.txt", "r") as read_file:
    contents = read_file.read()
    print(contents)
