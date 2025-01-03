# ------------------------------------------------------
# File: sys_module_functions.py
# Date: 2025-01-03
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Demonstrate usage of sys module: command-line arguments and memory size of an object

# This script demonstrates the use of the sys module to handle command-line arguments.
# To run this script, open a terminal/command prompt and use the following command:
# python script.py <arg1> <arg2> ...
# Example: python script.py 10 20 30
# Here, 'script.py' is the name of the script, and '10', '20', '30' are the arguments passed to it.
# The script will display the script name, the number of arguments (excluding the script name),
# and the list of arguments passed.


import sys

def square(sq):
    """Print the square of a number."""
    print(f"The square of the number {sq} is {sq ** 2}")

if __name__ == "__main__":
    try:
        # Check if the user provided enough command-line arguments
        if len(sys.argv) < 2:
            print("Usage: python script.py <number>")
        else:
            # Parse the first command-line argument as an integer
            num1 = int(sys.argv[1])
            
            # Display command-line arguments
            print(f"Script name: {sys.argv[0]}")
            print(f"Number of arguments: {len(sys.argv) - 1}")
            print(f"Argument list: {sys.argv[1:]}")
            
            # Perform square operation and display the memory size of the variable
            square(num1)
            print(f"The size of input variable 'num1' is {sys.getsizeof(num1)} bytes")
    
    except ValueError:
        print("Invalid input. Please provide a valid integer as a command-line argument.")
