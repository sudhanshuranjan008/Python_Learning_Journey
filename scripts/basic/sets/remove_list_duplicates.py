# ------------------------------------------------------
# File: remove_list_duplicates.py
# Date: 2024-12-11
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Remove all duplicates from a list using a set

# Original list with duplicates
runs = [45, 54, 25, 65, 45, 25]

# Convert the list to a set to remove duplicates, then convert it back to a list
updated_runs = list(set(runs))

# Display the original list and the updated list
print("List with duplicate values is: ", runs)
print("Updated list after duplicate removal is: ", updated_runs)

# Other method: To preserve the order of list

# Initialize an empty set to track seen elements
runs_set = set()
updated_in_order_runs = []
for run in runs:
    if run not in runs_set:
        updated_in_order_runs.append(run)
        # Add the element to the set to mark it as seen
        runs_set.add(run)

# Print the updated list, which preserves the original order of elements
print("Updated list with no duplicates and in original order is: ", updated_in_order_runs)
