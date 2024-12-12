# ------------------------------------------------------
# File: sort_dictionary.py
# Date: 2024-12-09
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Sort a dictionary by keys and values.

# Original dictionary
Players = {
    "P1": "Sachin",
    "P2": "Dhoni",
    "P4": "Virat",
    "P6": "Rohit",
    "P3": "Dravid",
    "P5": "Ganguly"
}

# Print original dictionary
print("Original Players dictionary:", Players)

# Sort by keys (default behavior)
players_sorted_by_keys = dict(sorted(Players.items()))  # Sorts based on keys
print("Dictionary sorted by keys:", players_sorted_by_keys)

# Sort by values using a lambda function
players_sorted_by_values = dict(sorted(Players.items(), key=lambda item: item[1]))  # Sorts based on values
print("Dictionary sorted by values:", players_sorted_by_values)
