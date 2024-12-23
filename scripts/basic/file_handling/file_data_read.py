# ------------------------------------------------------
# File: file_data_read.py
# Date: 2024-12-23
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Read a file and count the number of lines and words

# Open the file in read mode
rf = open("practice.txt", "r")  

# Initialize counters for lines and words
lines_count = 0
word_count = 0

# Iterate through the file line by line
# Each iteration processes one line at a time
for line in rf:
    lines_count += 1  # Increment line count for each line read
    # Split the line into words and count them
    # line.split() breaks the line into a list of words based on whitespace
    word_count += len(line.split())  

# Print the total counts
print("Number of lines in the text file:", lines_count)
print("Number of words in the text file:", word_count)

# Close the file after processing to free up resources
rf.close()

