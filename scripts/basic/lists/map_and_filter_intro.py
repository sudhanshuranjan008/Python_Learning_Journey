# ------------------------------------------------------
# File: map_and_filter_intro.py
# Date: 2025-01-09
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Demonstrate the use of map() and filter() with lists

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List of tuples containing (number, square of the number)
squares = [(x, x**2) for x in numbers]

# Use map() to extract only the square values from the list of tuples
numbers_square = map(lambda x: x[1], squares)
print(f"Squares of numbers: {list(numbers_square)}")

# Use filter() to extract only even numbers from the list
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(f"Even numbers: {list(even_numbers)}")
