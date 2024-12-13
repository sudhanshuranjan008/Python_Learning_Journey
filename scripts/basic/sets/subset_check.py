# ------------------------------------------------------
# File: subset_check.py
# Date: 2024-12-11
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Check if one set is a subset of another

# Using the intersection operator to check for subset
A = {1, 2, 3, 4, 5, 6, 7, 8, 9}  # Define the larger set A
B = {2, 3, 5, 7}  # Define the smaller set B

if A & B == B:  # Check if all elements of B are in the intersection of A and B
    print(f"Set {B} is a subset of set {A}")
else:
    print(f"Set {B} is not a subset of set {A}")


# Using built-in method
names = {"Ram", "Shyaam", "Virat", "Rohit", "Shreyas"}  # Define a set of names
cricketers = {"Rohit", "Virat", "Shreyas"}  # Define a set of cricketers

# Check if 'cricketers' is a subset of 'names' using the 'issubset()' method
if cricketers.issubset(names):  
    print(f"Set {cricketers} is a subset of set {names}")
else:
    print(f"Set {cricketers} is not a subset of set {names}")



# Using operator (<=) method
actors = {"Akshay", "Kartik", "Amir"}  # Define a set of actors

# Check if 'actors' is a subset of 'names' using the subset operator (<=)
if actors <= names:  
    print(f"Set {actors} is a subset of set {names}")
else:
    print(f"Set {actors} is not a subset of set {names}")
