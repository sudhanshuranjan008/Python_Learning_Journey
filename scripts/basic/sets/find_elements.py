# ------------------------------------------------------
# File: find_elements.py
# Date: 2024-12-12
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find elements in one set but not in another

alphabet = set(("a", "b", "c", "d", "e", "f", "g", "h", "i"))
vowels = {"a", "e", "i", "o", "u"}
missing_elements = set()

# Iterate through the alphabet set
for el in alphabet:
    # If an element is in alphabet but not in vowels, add it to missing_elements
    if el not in vowels:
        missing_elements.add(el)

# Iterate through the vowels set
for el in vowels:
    # If an element is in vowels but not in alphabet, add it to missing_elements
    if el not in alphabet:
        missing_elements.add(el)

# Print the resulting set of missing elements
print("The elements present in one set but not in another are: ", missing_elements)

# Using Set Method symmetric_difference() {^} operator

missing_elements_sym_diff = vowels.symmetric_difference(alphabet)
print("The elements present in one set but not in other using symmetric difference method are: ", missing_elements_sym_diff)
