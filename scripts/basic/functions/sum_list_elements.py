# ------------------------------------------------------
# File: sum_list_elements.py
# Date: 2024-12-16
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Create a function to calculate the sum of all elements in a list

# Function to calculate the sum of all elements in a list
def list_item_sum(thislist):
    # Check if the list is empty; return 0 if it is
    if len(thislist) == 0:
        return 0
    
    # Initialize the variable to store the sum of the list items
    list_sum = 0
    
    # Iterate through each item in the list and add it to the total sum
    for item in thislist:
        list_sum += item  # Add the current item to the cumulative sum
    
    # Return the total sum after the loop has completed
    return list_sum

# Main block that runs the program
if __name__ == "__main__":
    # Sample list of numbers
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Call the function to calculate the sum of the list
    mylistsum = list_item_sum(mylist)
    
    # Print the result of the sum calculation
    print("The sum of the elements of list is:", mylistsum)
