# ------------------------------------------------------
# File: pandas_intro.py
# Date: 2025-01-04
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Create a DataFrame from a dictionary and perform basic operations using pandas:
# Add a new column.
# Filter rows based on a condition

import pandas as pd  # Import the pandas library

# Create a dictionary with fruit names and their corresponding prices
mydict = {
    "Fruits": ["Apple", "Orange", "Kiwi", "Banana"],
    "Price" : [100, 80, 120, 30]
}

# Convert the dictionary into a pandas DataFrame
df = pd.DataFrame(mydict)

# Print the original DataFrame to the console
print("Original DataFrame is as below: \n", df)

# Add a new row to the DataFrame using pd.concat (alternative to df.loc[len(df)])
new_row = pd.DataFrame({"Fruits": ["Papaya"], "Price": [60]})  # Define the new row
df = pd.concat([df, new_row], ignore_index=True)  # Concatenate the new row to the existing DataFrame

# Print the updated DataFrame after adding the new row
print("DataFrame after update is as below: \n", df)

# Filter the DataFrame to show only fruits with a price greater than 100
filtered_df = df[df["Price"] > 100]

# Print the filtered DataFrame with fruits that have a price greater than 100
print("Fruits having price more than 100 are: \n", filtered_df["Fruits"])
