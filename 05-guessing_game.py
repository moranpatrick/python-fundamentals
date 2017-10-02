# Problem 5 - Write a guessing game where the user must guess a secret number.
#  After every guess the program tells the user whether their number was too large or too small. 
# At the end the number of tries needed should be printed. 
# It counts only as one try if they input the same number multiple times consecutively.

# Author - Patrick Moran g00179039

import random

# Generate a random number between 1 and 10
number = random.randint(1, 10)
num_tries = [] # to count the number of tries

print("Lets Begin The Guessing Game!")

while True:
    print("Guess a number between 1 and 10!")
    guess = int(input())

    # If its not a number between 1 and 10 it doesn't count as a try
    if guess < 0 or guess > 10:       
        print("Nope! Try a number between and 1 and 100!")
    elif guess in num_tries:
        print("Allready guessed %d! Don't worry it won't count as a guess!" % guess) # Allready guessed this number
    else:
        if guess > number: # If the guess is greater 
            num_tries.append(guess)
            print("Too High, try a Lower Number!")
        elif guess < number: # If the guess is lower
            num_tries.append(guess)
            print("To Low, think bigger!")
        else:   
            num_tries.append(guess) # Successfully Guessed  
            print("Success! It took you %s attempts to guess the number!" % str(len(num_tries)))
            break   # End Loop

    
# References:
# https://inventwithpython.com/chapter4.html

