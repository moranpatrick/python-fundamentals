# Problem 6 - Source: https://adriann.github.io/programming_problems.html
# Write a function that returns the largest and smallest elements in a list.

# Author: Patrick Moran g00179039

import random

random_list = [] # Array to hold the list of numbers

# Get the biggest and smallest numbers in the list using min and max functions
def sort(list):
    biggest = max(list)
    smallest = min(list)
    print("The Largest Number in the list is: %d.\nThe Smallest number in the list is: %d." % (biggest, smallest))

# Get the biggest and smallest numbers in the list using a loop
def sortWithLoop(list):
    max = 0
    min = 100
    for i in list:
        if i > max:
            max = i
        if i < min:
            min = i
    print("The largest number in the list is %d" % max)
    print("The smallest number in the list is %d" % min)

# Create a list of 10 random numbers from 1 to 100
for i in range (10):
    random_list.append(random.randrange(1,101,1))

# Print off the list
print (random_list)

# Call both functions passing in the random list 
sort(random_list)
sortWithLoop(random_list)

# References
# https://stackoverflow.com/questions/16655089/python-random-numbers-into-a-list
# https://stackoverflow.com/questions/3090175/python-find-the-greatest-number-in-a-list-of-numbers