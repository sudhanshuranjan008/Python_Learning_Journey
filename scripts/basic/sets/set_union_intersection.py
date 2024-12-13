# ------------------------------------------------------
# File: set_union_intersection.py
# Date: 2024-12-11
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

#Find the union and intersection of two sets.

# Find the union and intersection of two sets manually using loops
fruits = {"apple", "orange", "banana", "mango"}  # Define a set of fruits
brands = set(("mango", "google", "apple", "amazon"))  # Define a set of brands

# Initialize empty sets for union and intersection
union_set = set()
intersection_set = set()

# Loop through the 'fruits' set
for x in fruits:
    union_set.add(x)  # Add each fruit to the union set
    if x in brands:  # Check if the current fruit is also in the 'brands' set
        intersection_set.add(x)  # If true, add to the intersection set

# Loop through the 'brands' set
for y in brands:
    union_set.add(y)  # Add each brand to the union set

# Print the results of union and intersection
print("Union of fruits and brands is: ", union_set)
print("Intersection of fruits and brands is: ", intersection_set)

#Efficient Method
# Using built-in Python functions to perform union and intersection
prime = {2, 3, 5, 7}  # Define a set of prime numbers
even = set((2, 4, 6, 8))  # Define a set of even numbers

# Perform union and intersection using set operators
print("Union of the sets prime and even is: ", prime | even)  # Union using '|'
print("Intersection of the sets prime and even is: ", prime & even)  # Intersection using '&'
