# ------------------------------------------------------
# File: numpy_array_transpose.py
# Date: 2024-12-29
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find the transpose of a given NumPy array

import numpy as np  # Import the NumPy library and alias it as np

# Create a 2D NumPy array with two rows and five columns
arr = np.array([[1, 2, 3, 4, 5], 
                [6, 7, 8, 9, 10]])

# Transpose the array: This operation swaps rows with columns
transposed_arr = arr.transpose()

# Print the original array
print("The given array is:\n", arr)

# Print the transposed array
print("The transposed array is:\n", transposed_arr)
