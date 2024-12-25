# ------------------------------------------------------
# File: word_replacement.py
# Date: 2024-12-25
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find and replace a word in a file

# Open the file in read mode and read all lines into a list
with open("practice.txt", "r") as input_file:
    lines = input_file.readlines()

# Create an empty list to store the modified lines
new_lines = []
for line in lines:
    # Replace occurrences of the target word "several" with "various" in each line
    line = line.replace("several", "various")
    # Append the modified line to the new list
    new_lines.append(line)

# Open the file in write mode and write the modified lines back to the file
with open("practice.txt", "w") as output_file:
    output_file.writelines(new_lines)

# Open the updated file in read mode to verify the changes
with open("practice.txt", 'r') as updated_file:
    contents = updated_file.read()
    # Print the updated content of the file
    print(contents)
