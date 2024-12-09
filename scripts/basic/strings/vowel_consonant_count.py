# ------------------------------------------------------
# File: vowel_consonant_count.py
# Date: 2024-12-01
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Count the number of vowels and consonants in a string
string = "Python Learning Journey"  # Input string
vowel_count = 0  # Initialize vowel count
cons_count = 0  # Initialize consonant count

# Loop through each character in the string
for i in string:
    if i.lower() in "aeiou":  # Check if character is a vowel (case-insensitive)
        vowel_count += 1  # Increment vowel count
    elif i.isalpha():  # Check if character is an alphabet and not a vowel
        cons_count += 1  # Increment consonant count

# Print the counts of vowels and consonants
print("Vowel count is " + str(vowel_count) + "\n" + "Consonant count is " + str(cons_count))
