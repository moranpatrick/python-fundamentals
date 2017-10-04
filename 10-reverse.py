# Problem 10 - Write a function to reverse a string.
# Author: Patrick Moran g00179039

def reverse(str):
    return str[::-1] # slice the string like in the palindrome problem


print("Enter a string to Reverse: ")
string = str(input()) # Ask user for a word

print(reverse(string))

# References
# https://stackoverflow.com/questions/931092/reverse-a-string-in-python