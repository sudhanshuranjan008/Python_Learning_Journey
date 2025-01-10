# ------------------------------------------------------
# File: sort_list_of_dicts.py
# Date: 2025-01-10
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Sort a list of dictionaries by a specific key

fruits = ["Apple", "Banana", "Orange", "Grapes", "Kiwi"]
prices = [180, 60, 80, 90, 120]

# Create a list of dictionaries directly using list comprehension
price_list = [{"fruit": fruit, "price": price} for fruit, price in zip(fruits, prices)]

# Sort the list of dictionaries by the "price" key in descending order
sorted_price_list = sorted(price_list, key=lambda item: item["price"], reverse=True)

# Print the list in a tabular form
print("Price list of fruits, sorted as per price is:")
for item in sorted_price_list:
    print(item)

