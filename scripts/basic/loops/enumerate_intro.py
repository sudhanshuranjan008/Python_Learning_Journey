# File: enumerate_intro.py
# Date: 2025-01-11
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Explore and use enumerate() with a for loop

# A list of subjects/topics to study
study = ["SQL", "Python", "DSA", "Spark", "Data Modeling"]

# Using enumerate() to iterate over the list with an index
# The 'start=1' ensures the indexing begins at 1 instead of the default 0
for index, sub in enumerate(study, start=1):
    # Printing each index and subject in the format: "index - subject"
    print(f"{index} - {sub}")
