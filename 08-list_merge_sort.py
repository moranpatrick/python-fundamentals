# Problem 8 - Source: https://adriann.github.io/programming_problems.html
# Write a function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6].

# Author: Patrick Moran g00179039

# Sort List Function
def sortLists(lst1, lst2):
    list = lst1 + lst2 # Merge The Two Lists
    list.sort()
    print(list)

# Variables
list1 = []
list2 = []

print("Enter your values for the first list, each followed with a space: ")
list1 = [int(x) for x in input().split()]
    
print("Enter your values for the second list, each followed with a space: ")
list2 = [int(x) for x in input().split()]

print(list1)
print(list2)

sortLists(list1, list2)

# References
# https://stackoverflow.com/questions/4663306/get-a-list-of-numbers-as-input-from-the-user
# https://stackoverflow.com/questions/1720421/how-to-concatenate-two-lists-in-python