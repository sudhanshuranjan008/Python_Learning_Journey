# ------------------------------------------------------
# File: zip_lists_to_dict.py
# Date: 2025-01-10
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Demonstrating the use of zip() to combine two lists into a dictionary

# Lists of fruits and prices
fruits = ["Apple", "Banana", "Orange", "Grapes", "Kiwi"]
price = [180, 60, 80, 90, 120, 32, 56]  # Intentionally longer list

# Warning for mismatched lengths
if len(fruits) != len(price):
    print(f"Warning: The lists have different lengths. Only {min(len(fruits), len(price))} items will be paired.")

# Combine the two lists into a dictionary
fruit_price = dict(zip(fruits, price))

# Display the resulting dictionary
print("\nFruit price dictionary:")
for fruit, price in fruit_price.items():
    print(f"{fruit}: {price}")
