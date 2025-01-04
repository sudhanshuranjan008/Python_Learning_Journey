# ------------------------------------------------------
# File: matplotlib_intro.py
# Date: 2025-01-04
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Plot a line graph and a bar chart for a given dataset using matplotlib

import matplotlib.pyplot as plt  # Import the matplotlib library for plotting

# Generate a list of numbers from 1 to 10
num = [x for x in range(1, 11)]

# Generate the squares of the numbers
num_square = [x*x for x in range(1, 11)]

# Plot a line graph
plt.figure(1)  # Create a new figure for the line graph
plt.plot(num, num_square, marker='o', linestyle='-', color='b', label="Squares")  # Plot numbers vs their squares
plt.title("Line Graph of Numbers and Their Squares")  # Set the title of the graph
plt.xlabel("Numbers")  # Label the x-axis
plt.ylabel("Squares")  # Label the y-axis
plt.legend()  # Add a legend to the graph
plt.grid(True)  # Enable gridlines for better readability
plt.show()  # Display the line graph

# Plot a bar chart
plt.figure(2)  # Create another figure for the bar chart
plt.bar(num, num_square, color='orange', label="Squares")  # Create a bar chart with orange bars
plt.title("Bar Chart of Numbers and Their Squares")  # Set the title of the bar chart
plt.xlabel("Numbers")  # Label the x-axis
plt.ylabel("Squares")  # Label the y-axis
plt.legend()  # Add a legend to the bar chart
plt.show()  # Display the bar chart
