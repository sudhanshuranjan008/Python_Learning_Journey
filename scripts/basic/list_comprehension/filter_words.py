# ------------------------------------------------------
# File: filter_words.py
# Date: 2024-12-26
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Filter out all words from a given list that start with the letter 'a'

# List of fruits
fruits = ["apple", "mango", "banana", "cherry", "papaya"]

# Filter out words that start with the letter 'a'
fruits_filtered = [x for x in fruits if not x.startswith("a")]  # List comprehension to filter words

# Print the filtered list
print(fruits_filtered)  # Output: ['mango', 'banana', 'cherry', 'papaya']
