# ------------------------------------------------------
# File: file_not_found.py
# Date: 2024-12-25
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Write a program to handle the file not found exceptions

try:
    # Prompt the user to enter the file name and open the file in read mode
    with open(input("Enter file name in .txt format: "), "r") as input_file:
        # Read the content of the file and print it
        content = input_file.read()
        print(content)

# Handle the case where the file is not found
except FileNotFoundError:
    print("File not found. Please ensure the file name is correct and try again.")

# Handle any other input/output related issues (like permission errors)
except IOError:
    print("An error occurred while trying to read the file.")

# Optional: Handle other possible exceptions like ValueError or general issues
except Exception as e:
    print(f"An unexpected error occurred: {e}")
