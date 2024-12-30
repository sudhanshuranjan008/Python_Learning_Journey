# ------------------------------------------------------
# File: class_creation.py
# Date: 2024-12-30
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Create a class Person with attributes name, age, and a method greet() that prints a greeting

# Define the Person class
class Person:
    # Constructor method to initialize the object's attributes
    def __init__(self, name, age):
        self.name = name  # Assign the name attribute
        self.age = age    # Assign the age attribute

    # Method to print a greeting message
    def greet(self):
        print(f"Hello! my name is {self.name}. I am {self.age} years old.")

# Create an instance of the Person class
p1 = Person("Iota", 2)  # Initialize with name "Iota" and age 2

# Call the greet method for the created instance
p1.greet()  # Output: Hello! my name is Iota. I am 2 years old.
