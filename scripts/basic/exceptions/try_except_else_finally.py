# ------------------------------------------------------
# File: try_except_else_finally.py
# Date: 2024-12-25
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement a program with try-except-else-finally blocks

# This program checks if a factor divides a number evenly.
while True:
    try:
        # Take input for the number and the potential factor.
        num = int(input("Enter a number: "))
        factor = int(input("Enter a number to check if it's a factor of the already input number: "))
        
        # Check if the factor is zero. Raise ZeroDivisionError if so.
        if factor == 0:
            raise ZeroDivisionError("Factor cannot be zero for division or modulo operations.")
        
        # Print the message about checking the factor.
        print(f"Let us check if {factor} is a factor of {num}.")
    
    except ValueError:
        # Handles the case where the user inputs a non-integer value.
        print("Please enter a valid integer number.")
    
    except ZeroDivisionError as e:
        # Catches the ZeroDivisionError raised for a factor of zero.
        print(e)

    else:
        # If no exceptions occurred, proceed with the logic.
        if num >= 0 and factor >= 0:
            if num % factor == 0:
                print(f"Yes!, {factor} is a factor of {num}.")
            else:
                print(f"{factor} is not a factor of {num}.")
        # Exit the loop once a valid input and check are done.
        break
    
    finally:
        # This block runs no matter what, to signify the attempt is completed.
        print("Attempt completed.")

