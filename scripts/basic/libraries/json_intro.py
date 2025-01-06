# ------------------------------------------------------
# File: json_intro.py
# Date: 2025-01-05
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Read a JSON file and convert it into a Python dictionary using JSON

import json

# Open the file in read mode and load the JSON content
with open("data.json", "r") as read_file:
    # Read the entire content of the file as a single string
    text = read_file.read()

# Convert the JSON string to a Python dictionary
mydict = json.loads(text)

# Print the dictionary
print(mydict)



