# ------------------------------------------------------
# File: uppercase_vowels.py
# Date: 2024-12-26
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Convert all vowels in a given string to uppercase using list comprehension

mystring = "listcomprehension"

# Convert vowels to uppercase using list comprehension
updated_mystring = ''.join([x.upper() if x in {"a", "i", "e", "o", "u"} else x for x in mystring])

# Output the updated string
print(updated_mystring)
