# ------------------------------------------------------
# File: element_frequency_in_list.py
# Date: 2024-12-03
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Count the frequency of each element in a list.

# Define the original list
mylist = [5, 3, 2, 5, 4, 3, 4, 1, 9, 8, 7, 7, 6, 6, 1, 6]
new_list = []  # To track already counted elements

for i in mylist:
    if i not in new_list:  # Check if element hasn't been counted yet
        count = mylist.count(i)  # Count occurrences of the element in the list
        print(f"Count of {i} in my list is: {count}")
        new_list.append(i)  # Add the element to new_list to avoid recounting it
