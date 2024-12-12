# ------------------------------------------------------
# File: word_count.py
# Date: 2024-12-09
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Count the frequency of each word in a sentence using a dictionary.

# Input sentence
sentence = "Einstein once said, Science without religion is lame, religion without science is blind."

# Remove punctuation (commas and periods) and convert the sentence to lowercase
sentence_clean = sentence.lower().replace(",", "").replace(".", "")

# Create an empty dictionary to store the word count
word_count = {}

# Split the cleaned sentence into words and iterate over each word
for word in sentence_clean.split():
    # Check if the word is already in the dictionary
    if word in word_count:
        # If it exists, increment the count by 1
        word_count[word] += 1
    else:
        # If it doesn't exist, add the word to the dictionary with a count of 1
        word_count[word] = 1

# Output the frequency of each word
print("Frequency of each word in sentence is: ", word_count)
