# ------------------------------------------------------
# File: file_append.py
# Date: 2024-12-23
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Append text to a file and display its content

# Open the file in append mode to add text at the end without overwriting
append_file = open("practice.txt", "a")
# Write a line of text to the file, with a newline character to ensure it's on a new line
append_file.write("I have added this line using file handling in python.\n")
# Close the file after writing
append_file.close()

# Open the file in read mode to read its contents
read_file = open("practice.txt", "r")
# Print the entire content of the file
print(read_file.read())
# Close the file after reading
read_file.close()
