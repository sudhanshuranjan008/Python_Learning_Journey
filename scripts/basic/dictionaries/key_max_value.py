# ------------------------------------------------------
# File: key_max_value.py
# Date: 2024-12-10
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

#Find the key with the maximum value in a dictionary

# Using a for loop to find the key with the maximum value
runs = {
    "P1": 52,
    "P2": 66,
    "P3": 85,
    "P4": 0,
    "P5": 45
}

max_key = None
max_value = 0

for key, value in runs.items():
    if value > max_value:
        max_value = value
        max_key = key

print("Using a loop; Key with maximum values in dictionary, run is: ", max_key)


#Using python methods max() and get()

# Define a dictionary where keys represent players and values represent their scores
runs = {
    "P1": 52,
    "P2": 66,
    "P3": 85,
    "P4": 0,
    "P5": 45
}

# Use the max() function to find the key with the maximum value
# 'key=runs.get' specifies that the values in the dictionary should be compared
max_key = max(runs, key=runs.get)

# Print the result
print("Using python functions; Key with maximum values in dictionary, run is: ", max_key)

