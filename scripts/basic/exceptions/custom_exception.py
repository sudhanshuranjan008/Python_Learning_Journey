# ------------------------------------------------------
# File: custom_exception.py
# Date: 2024-12-25
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Create a program to raise a custom exception if a number is negative

# Function to check if the number is positive, negative, or zero
def check_number(num):
    # Raise an exception if the number is negative
    if num < 0:
        raise Exception("The number is negative. Please enter a positive number.")
    # Print a message if the number is zero
    elif num == 0:
        print("0 is neither positive nor negative.")
    # Print the number if it's positive
    else:
        print(f"The number is {num}")

# Main block of the program
if __name__ == "__main__":
    try:
        # Prompt the user to input a number
        num = int(input("Enter a positive number: "))
        # Call the function to check the number
        check_number(num)
    except ValueError:  # Catch and handle invalid input (non-integer values)
        print("Invalid input. Please enter an integer.")
    except Exception as NegativeError:  # Catch and handle the custom exception raised in the function
        print(NegativeError)

