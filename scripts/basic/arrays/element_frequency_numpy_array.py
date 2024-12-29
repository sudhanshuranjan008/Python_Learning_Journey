# ------------------------------------------------------
# File: element_frequency_numpy_array.py
# Date: 2024-12-29
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Count the frequency of a specific element in a NumPy array

import numpy as np  # Import the NumPy library and alias it as np

# Define a NumPy array with multiple elements
arr = np.array([2, 5, 6, 8, 3, 2, 4, 5, 8, 5, 2])

# Use np.count_nonzero to count how many times 2 appears in the array
el_count = np.count_nonzero(arr == 2)

# Print the frequency of number 2 in the array
print("The frequency of number 2 in the array is:", el_count)
