# ------------------------------------------------------
# File: string_replacement.py
# Date: 2024-12-01
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Replace all occurrences of a substring with another substring
string = '''I am learning to code in language. Language has many use cases. 
The more you code the better you get in language.'''  # Input string with substrings to replace

# Replace all occurrences of 'language' (case-insensitive) with 'python'
rep_string = string.replace('language', 'python')  # Replace 'language' with 'python'
rep_string = rep_string.replace('Language', 'Python')  # Replace 'Language' with 'Python' (case-sensitive)

# Print the updated string
print(rep_string)
