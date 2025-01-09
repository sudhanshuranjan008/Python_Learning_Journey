# ------------------------------------------------------
# File: basic_string_manipulation.py
# Date: 2025-01-09
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Use split() and join() to manipulate strings

input_string = "to be or not to be"

# Split the string into words
split_string = input_string.split()

# Replace specific words and join back
styled_string = ' '.join(
    word.replace('to', '2').replace('be', 'B') for word in split_string
)

# Print the original and styled strings
print(f"'{input_string}', can be styled and also be written as, '{styled_string}'")
