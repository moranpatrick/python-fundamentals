# Problem 8 - Source: https://adriann.github.io/programming_problems.html
# Write a function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6].

# Author: Patrick Moran g00179039

# Sort List Function
def sortLists(lst1, lst2):
    list = lst1 + lst2 # Merge The Two Lists
    list.sort() # Sort the Merged List
    print(list) # Print The Sorted List

# Variables
list1 = []
list2 = []

print("Enter your values for the first list (No Spaces):")
l1 = input()
list1 = list(map(int, l1)) # Covert th input into a list using map()
    
print("Now Enter your values for the second list(No Spaces):")
l2 = input()
list2 = list(map(int, l2))

print(list1)
print(list2)

# Sort Both Lists
sortLists(list1, list2)

# References
# https://stackoverflow.com/questions/29409273/how-to-split-string-without-spaces-into-list-of-integers-in-python
# https://stackoverflow.com/questions/1720421/how-to-concatenate-two-lists-in-python