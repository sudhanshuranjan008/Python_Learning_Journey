# ------------------------------------------------------
# File: remove_dict_item.py
# Date: 2024-12-10
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Remove a key-value pair from a dictionary

marks_sheet = {
    "Maths": "98",
    "English": "85",
    "Geography": "91",
    "Biology": "81",
    "Economics": "90"
}

# Display the original dictionary
print("Original dictionary: ", marks_sheet)

# Check if the key exists before removing it
if "Geography" in marks_sheet:
    removed_value = marks_sheet.pop("Geography")  # Safely remove the key
    print(f"Removed 'Geography' with value: {removed_value}")
else:
    print("Key 'Geography' not found in the dictionary!")

# Display the updated dictionary
print("Dictionary after deleting an item: ", marks_sheet)
