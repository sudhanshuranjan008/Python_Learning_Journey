# ------------------------------------------------------
# File: max_min_in_list.py
# Date: 2024-12-02
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Find the largest and smallest numbers in a list.

# List of scores
score = [22, 45, 76, 89, 24, 43]

# Initialize min and max to the first element of the list
min = score[0]
max = score[0]

# Iterate through the list to find the largest and smallest numbers
for x in score:
    # If the current number is larger than max, update max
    if x > max:
        max = x
    # If the current number is smaller than min, update min
    elif x < min:
        min = x

# Print the largest and smallest scores
print("The largest score is ", max)
print("The smallest score is ", min)


# Other way: Using sorted() to find the largest and smallest numbers.

# List of numbers
num = [1, 5, 66, 45, 8, 13, 58]

# Sort the list in ascending order using sorted(), returns a new sorted list
sorted_num = sorted(num)

# Print the largest number (last element in the sorted list)
print("The largest number is ", sorted_num[-1])

# Print the smallest number (first element in the sorted list)
print("The smallest number is ", sorted_num[0])
