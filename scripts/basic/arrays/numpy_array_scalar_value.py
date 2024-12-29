# ------------------------------------------------------
# File: numpy_array_scalar_value.py
# Date: 2024-12-29
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Add a scalar value to each element of a NumPy array

import numpy as np  # Use the community-accepted alias

# Create a NumPy array with values from 0 to 6
arr = np.arange(7)

# Add a scalar value of 5 to each element
updated_arr = arr + 5

# Print the original and updated arrays
print("The original array is:", arr)
print("The array after adding a scalar value of 5 to each element is:", updated_arr)

