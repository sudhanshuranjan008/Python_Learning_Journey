# ------------------------------------------------------
# File: split_list.py
# Date: 2024-12-04
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Split a list into chunks of n size.

# Define the list to be chunked
mylist = [54, 61, 78, 88, 21, 541, 6541, 7, 3, 2, 45, 86]

# Input chunk size from the user
n = int(input("Enter the size in which you want your list to be chunked:"))

# Loop through the list in steps of 'n' to create chunks
for i in range(0, len(mylist), n):
    # Slice the list from the current index 'i' to 'i + n'
    print(mylist[i:i + n])  # Print the current chunk

