# ------------------------------------------------------
# File: disjoint_sets.py
# Date: 2024-12-12
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Define two sets, flower and fruits
flower = {"Rose", "Jasmine", "Hibiscus", "Marigold", "Lotus"}  # Set of flowers
fruits = set(("Apple", "Papaya", "Grapes", "Watermelon", "Banana"))  # Set of fruits

# Find common elements using the intersection operator (&)
common_elements = flower & fruits

# Check if the intersection is empty
if len(common_elements) == 0:  # If no common elements, sets are disjoint
    print("flower and fruits are disjoint sets")
else:  # Otherwise, sets are not disjoint
    print("flower and fruits are not disjoint sets and have common elements: ", common_elements)


# Check if two sets are disjoint using isdisjoint() method
if flower.isdisjoint(fruits):
    print("flower and fruits are disjoint sets")
else:
    print("flower and fruits are not disjoint sets and have common elements")

