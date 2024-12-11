# ------------------------------------------------------
# File: merge_sorted_lists.py
# Date: 2024-12-02
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Merge two sorted lists into one sorted list.

# Method 1: Using `extend()` and `sorted()`
# This method first merges the two lists and then sorts the combined list.

list1 = [15, 24, 42, 56, 84, 226]
list2 = [15, 45, 54, 56, 58, 226]

# Step 1: Merge list2 into list1 using `extend()`
list1.extend(list2)

# Step 2: Sort the combined list
# Sorting the list after merging is O((n + m) log(n + m)) where n is the length of list1 and m is the length of list2.
merged_list = sorted(list1)

# Step 3: Print the result
print("Sorted merged list is: ", merged_list)


# Method 2: Merging Two Sorted Lists Efficiently
# This method merges the two lists in sorted order without needing to sort the merged list.
# Time complexity: O(n + m), where n is the size of list1 and m is the size of list2.

list1 = [15, 24, 42, 56, 84, 226]
list2 = [15, 45, 54, 56, 58, 226]

# Step 1: Initialize an empty list to store the merged result
merged_list = []

# Step 2: Use two pointers (i and j) to traverse both lists
i, j = 0, 0

# While loop compares the current elements in both lists and appends the smaller element to the merged list.
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merged_list.append(list1[i])
        i += 1  # Move the pointer in list1
    else:
        merged_list.append(list2[j])
        j += 1  # Move the pointer in list2

# Step 3: Append the remaining elements from both lists (if any)
# If there are elements left in list1, extend merged_list with the rest of list1
merged_list.extend(list1[i:])
# If there are elements left in list2, extend merged_list with the rest of list2
merged_list.extend(list2[j:])

# Step 4: Print the efficiently merged sorted list
print("Efficiently merged sorted list is: ", merged_list)

