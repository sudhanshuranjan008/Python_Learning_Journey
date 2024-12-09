# ------------------------------------------------------
# File: string_reversal.py
# Date: 2024-12-01
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Reverse a string in multiple ways

# Original string
string = "Python Leraning Journey"

# 1. Using slicing
# Slicing syntax [start:end:step] with step -1 reverses the string
print(string[::-1])  # Output: yenruoJ gninareL nohtyP

# 2. Using the reversed() function
# reversed() creates an iterator that traverses the string in reverse order
# ''.join() concatenates the characters into a single reversed string
rev = ''.join(reversed(string))
print(rev)  # Output: yenruoJ gninareL nohtyP

# 3. Using a for loop (manual reversal)
# Loop through each character in the string
# Prepend each character to the result string to reverse it
loop_rev = ''
for ch in string:
    loop_rev = ch + loop_rev
print(loop_rev)  # Output: yenruoJ gninareL nohtyP

# 4. Using a for loop with indexing
# range(start, stop, step) generates indices from the end to the start
# Access each character using its index and concatenate them in reverse order
list_rev = ''.join(string[i] for i in range(len(string)-1, -1, -1))
print(list_rev)  # Output: yenruoJ gninareL nohtyP
