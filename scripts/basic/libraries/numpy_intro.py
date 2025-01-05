# ------------------------------------------------------
# File: numpy_intro.py
# Date: 2025-01-05
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Perform matrix multiplication between two arrays using NumPy

import numpy as np

# Define the first array
arr1 = np.array([[x for x in range(1, 5)], [x * x for x in range(1, 5)]])
print("Array 1:\n", arr1)

# Define the second array
arr2 = np.array([[1, 2, 3, 4], [2, 4, 6, 8]])
print("Array 2:\n", arr2)

# Perform matrix multiplication
# Transpose arr2 to align the dimensions for matrix multiplication
arr_product = np.matmul(arr1, arr2.T)
print("Matrix Multiplication Result:\n", arr_product)
