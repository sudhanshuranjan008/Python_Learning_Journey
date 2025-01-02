# ------------------------------------------------------
# File: os_module_methods.py
# Date: 2025-01-02
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Write a program to list all files in the current directory. Also, create and delete a directory using os module.

# Import the os module for interacting with the operating system
import os

# List all files and folders in the current working directory
dir_list = os.listdir() 
print(f"All the files in the current working directory are listed below: \n {dir_list}")

# Create a new directory named "test"
os.mkdir("test")
print(f"Directory 'test' created successfully.")

# List files and folders again to show the updated state after creating the directory
print(f"Updated files and folders in the current directory are: \n {os.listdir()}")

# Remove the directory named "test"
os.rmdir("test")
print(f"Directory 'test' deleted successfully.")

# List files and folders again to show the updated state after deleting the directory
print(f"Updated files and folders in the current directory are: \n {os.listdir()}")
