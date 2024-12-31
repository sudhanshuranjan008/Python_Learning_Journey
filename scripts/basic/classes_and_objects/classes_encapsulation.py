# ------------------------------------------------------
# File: classes_encapsulation.py
# Date: 2024-12-31
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Write a program to demonstrate encapsulation by making an attribute private and providing getter and setter methods

class PreSchool:
    def __init__(self, age: int):
        # Initializer to set the private attribute '__age'
        # The age will be a private attribute, and is set through the constructor
        self.__age = age

    @property
    def age(self):
        """
        Getter method to retrieve the age of the child.
        This is the basic getter, allowing access to the '__age' attribute
        as if it were a public attribute.
        """
        return self.__age

    @age.getter
    def age(self):
        """
        This is the additional getter method that provides a custom message.
        It gives a more informative response when the 'age' property is accessed.
        """
        return f"The age of the kid is {self.__age} and it is recommended to join pre-school."

    @age.setter
    def age(self, new_age: int):
        """
        Setter method to validate and set the age of the child.
        - It checks if the input is an integer.
        - It ensures that the age is between 3 and 5 (valid pre-school age).
        If the validation fails, it raises an exception.
        """
        # Check if the new_age is an integer
        if not isinstance(new_age, int):
            raise TypeError("Age must be an integer.")  # Raise error if not an integer

        # Validate if the new_age is within the pre-school range (3 to 5 years old)
        if 3 <= new_age <= 5:
            self.__age = new_age  # If valid, set the age
        else:
            raise ValueError("Invalid age for pre-school.")  # Raise error if not in valid range
    

# Create an instance of the PreSchool class with an initial age of 4
kid1 = PreSchool(4)

# Set age using the setter method
kid1.age = 5  # This will trigger the setter, and validate the new age

# Print the age using the getter method
# The getter will return a custom message, as the @age.getter method is defined
print(kid1.age)  # Output: The age of the kid is 5 and it is recommended to join pre-school.


