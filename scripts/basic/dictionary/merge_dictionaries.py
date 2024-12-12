# ------------------------------------------------------
# File: merge_dictionaries.py
# Date: 2024-12-09
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Merge two dictionaries using different methods

# Dictionary definitions
car1 = {
    "name": "I20",
    "color": "Red",
    "brand": "Hyundai"
}

car2 = dict(name="Brezza", color="Blue", brand="Suzuki")
car3 = dict(name="Fortuner", color="Black", brand="Toyota")

feat1 = dict(fuel_type="Petrol", categ="Hatchback")
feat2 = dict(fuel_type="Diesel", categ="Compact-SUV")
feat3 = dict(fuel_type="Petrol", categ="SUV")

# Method 1: Using update()
car1.update(feat1)  # Modifies car1 in-place
print("Merged using update():", car1)

# Method 2: Using the | operator (Python 3.9+)
car2 = car2 | feat2  # Creates a new dictionary
print("Merged using | operator:", car2)

# Method 3: Using dictionary unpacking (Python 3.5+)
car3 = {**car3, **feat3}  # Creates a new dictionary
print("Merged using dictionary unpacking:", car3)
