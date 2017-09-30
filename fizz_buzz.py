# Problem 3 - Write a program that prints the numbers from 1 to 100, except for the following conditions. 
# For multiples of three print “Fizz” instead of the number, and for the multiples of five print “Buzz”. 
# For numbers which are multiples of both three and five print “FizzBuzz”.

# Author - Patrick Moran g00179039

# Create a for loop from 1 to 100
for i in range(1,101):
    #Firstly if the number is divisible by 3 and 5 then print fizz buzz
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    # If the number is divisible by 3 print fizz
    elif i % 3 == 0:
        print("Fizz")
    # If the number is divisible by 5 print buzz
    elif  i % 5 == 0:
        print("Buzz")
    # Otherwise Print the number to the Screen
    else:
        print(i)


# References
# http://wiki.c2.com/?FizzBuzzTest

    
