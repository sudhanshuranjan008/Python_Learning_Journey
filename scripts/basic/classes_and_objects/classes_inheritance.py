# ------------------------------------------------------
# File: classes_inheritance.py
# Date: 2024-12-30
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Create a Vehicle class and then a Car class that inherits from Vehicle and adds a fuel_type attribute

# Class Vehicle defines a general vehicle with a name attribute
class Vehicle():
    # The __init__ method initializes the name of the vehicle
    def __init__(self, name: str):
        self.name = name  # Set the name attribute for the Vehicle object

# Class Car inherits from Vehicle, meaning it gets the 'name' attribute from Vehicle
class Car(Vehicle):
    # The __init__ method initializes both 'name' (from Vehicle) and 'fuel_type' (specific to Car)
    def __init__(self, name: str, fuel_type: str):
        super().__init__(name)  # Call the parent class constructor to set the 'name'
        self.fuel_type = fuel_type  # Set the fuel_type attribute for the Car object
    
    # This method prints the details of the car, specifically its fuel type
    def print_details(self):
        print(f"Fuel type of car {self.name} is {self.fuel_type}.")
    
    # The __str__ method returns a user-friendly string representation of the Car object
    def __str__(self):
        return f"Car {self.name} runs on {self.fuel_type}."

# Creating a Car object called car1 with the name "BMW X7" and fuel type "Petrol"
car1 = Car("BMW X7", "Petrol")

# Calling the print_details method to print the car's fuel type
car1.print_details()  # This will print: Fuel type of car BMW X7 is Petrol.

# Calling the __str__ method indirectly by printing the object
print(car1)  # This will print: Car BMW X7 runs on Petrol.
