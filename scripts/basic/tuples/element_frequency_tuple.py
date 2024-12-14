# ------------------------------------------------------
# File: element_frequency_tuple.py
# Date: 2024-12-13
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Count the frequency of an element in a tuple
fruits = ("Apple", "Banana", "apple", "banana", "grapes", "GRAPES", "bERRY", "Berry")

# Convert all elements to lowercase for case-insensitive comparison
lowercase_fruits = [item.lower() for item in fruits]

# Find unique elements using a list and count their occurrences
unique_fruits = []
for item in lowercase_fruits:
    if item not in unique_fruits:
        count = lowercase_fruits.count(item)
        print(f"The count of '{item}' in the tuple fruit is {count}")
        unique_fruits.append(item)


# Other method using set() and list()

# Count the frequency of an element in a tuple
fruits2 = ("Apple", "Banana", "apple", "banana", "grapes", "GRAPES", "bERRY", "Berry", "MeLon", "papaYA")

# Convert all elements to lowercase for case-insensitive comparison
lowercase_fruits2 = [item.lower() for item in fruits2]

# Use a set to find unique elements and count their occurrences
for fruit in set(lowercase_fruits2):
    count = lowercase_fruits2.count(fruit)
    print(f"The count of '{fruit}' in the tuple fruits2 is {count}")

