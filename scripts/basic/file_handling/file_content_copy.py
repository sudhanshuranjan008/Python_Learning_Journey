# ------------------------------------------------------
# File: file_content_copy.py
# Date: 2024-12-25
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Copy the content of one file into another

# Copy the content of one file into another, line by line
with open("practice.txt", "r") as input_file, open("practice_copy.txt", "w") as copy_file:
    for line in input_file:
        copy_file.write(line)

# Verify the copied content
with open("practice_copy.txt", "r") as new_file:
    content_copy = new_file.read()
    print(content_copy)
