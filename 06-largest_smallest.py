# Problem 6 - Source: https://adriann.github.io/programming_problems.html
# Write a function that returns the largest and smallest elements in a list.

# Author: Patrick Moran g00179039

import random

random_list = [] # Array to hold the list of numbers

# Sort List using min and max functions
def sort(list):
    biggest = max(list)
    smallest = min(list)

    print("The Largest Number in the list is: %d.\nThe Smallest number in the list is: %d." % (biggest, smallest))

# Create a list of 10 random numbers from 1 to 100
for i in range (10):
    random_list.append(random.randrange(1,101,1))

# Print off the list
print (random_list)
sort(random_list)



# References
# https://stackoverflow.com/questions/16655089/python-random-numbers-into-a-list
# https://stackoverflow.com/questions/3090175/python-find-the-greatest-number-in-a-list-of-numbers