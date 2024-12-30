# ------------------------------------------------------
# File: classes_polymorphism.py
# Date: 2024-12-30
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement polymorphism by creating two classes Dog and Cat with a method speak().
# -----------------Write a function that calls the speak() method for both classes

# Define a class for Dog
class Dog:
    def __init__(self, voice: str):  # Initialize the Dog class with a voice attribute
        self.voice = voice

    def speak(self):  # Method to print the voice of the Dog
        print(f"A Dog's voice is '{self.voice}'.")

# Define a class for Cat
class Cat:
    def __init__(self, voice: str):  # Initialize the Cat class with a voice attribute
        self.voice = voice

    def speak(self):  # Method to print the voice of the Cat
        print(f"A Cat's voice is '{self.voice}'.")

# Create instances of Dog and Cat with specific voices
pet1 = Dog("bark")
pet2 = Cat("meow") 

# Loop through the pet objects and call their speak methods
for x in (pet1, pet2):  # Demonstrates polymorphism by calling the speak method of both objects
    x.speak()
