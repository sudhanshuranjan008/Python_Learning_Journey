# ------------------------------------------------------
# File: symmetric_difference.py
# Date: 2024-12-12
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find the symmetric difference between two sets

set1 = {5, 8, 45, 65, 12, 33}  # First set
set2 = {56, 65, 12, 6, 22, 33, 11}  # Second set

# Find the symmetric difference using the ^ operator
# Symmetric difference: Elements in either set1 or set2, but not in both
print("The symmetric difference between two sets is: ", set1 ^ set2)
