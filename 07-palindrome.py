# Problem 7 - Source: https://adriann.github.io/programming_problems.html
# Write a function that tests whether a string is a palindrome.

# Author: Patrick Moran g00179039

# Function to check if a word is a palindrome
def palindromeCheck(str):   
    str = str.lower() # Convert string to lowercase
    str = ''.join(char for char in str if char.isalpha()) # Using char.isalpha() lets you ignore everything that's not a letter

    # Now check if the string is a palindrome
    if str == str[::-1]:
        return True
    else:
        return False

print("Palindrome Test!")
print("Enter a string to check if its a Palindrome. Don't worry about punctuation, cap locks or spaces!: ")
string = str(input()) # Ask user for a word

if palindromeCheck(string) == True:
    print("The String \"%s\" is a palindrome!" % string)
else:
    print("The String \"%s\" is not a plaindrome!" % string)
    
# Some Examples of palindromes you can try
# madam
# A dog! A panic in a pagoda!
# A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!
# “Cain, a motor erotomaniac was Eve,” said I as Eve saw Cain, “a motor erotomaniac!”

# References
# https://stackoverflow.com/questions/17331290/how-to-check-for-palindrome-using-python-logic (Testing a word)
# https://stackoverflow.com/questions/25882015/python-check-if-a-string-is-palindrome-or-not (Testing a long string)
# http://www.palindromelist.net/ (Examples of Palindromes)