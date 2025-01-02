# ------------------------------------------------------
# File: math_on_circle.py
# Date: 2025-01-02
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Write a script using the math module to calculate the area and circumference of a circle

# Import the math module to access mathematical constants and functions
import math

# Define a function to calculate the area of a circle given its radius
def area_of_circle(r):
    return (math.pi * r * r)

# Define a function to calculate the circumference of a circle given its radius
def circumference_of_circle(r):
    return (2 * math.pi * r)

# Main block of code to execute the script
if __name__ == "__main__":
    while True:  # Use a loop to allow repeated input in case of invalid entries
        try:
            # Prompt the user to input the radius of the circle
            radius = float(input("Enter the radius of the circle: "))
            
            # Check for negative radius values
            if radius < 0:
                print("Radius cannot be negative. Please enter a positive integer.")
            
            else:
                # Calculate and display the area and circumference, rounded to 2 decimal places
                print("Area of circle is ", round(area_of_circle(radius), 2))
                print("Circumference of circle is ", round(circumference_of_circle(radius), 2))
                break  # Exit the loop after successfully displaying the results
        
        # Handle invalid input such as non-numeric values
        except ValueError:
            print("Invalid input. Please enter a positive number.")
