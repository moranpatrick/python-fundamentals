# Problem 4 - Write a function that calculates the sum of the digits of the factorial of a number. 
# n! means n x (n − 1) … x 3 x 2 x 1. For example, 10! = 10 x 9 x … x 3 x 2 x 1 = 3628800, 
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27. 
# Find the sum of the digits in the number 100!

# Author - Patrick Moran g00179039

# This Function will calculate the factorial value of a number entered
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

# Using the sum and map function together the sum of the digits from the answer can be calculated
digit_sum = sum(map(int, str(factorial(100))))

print(digit_sum) # Print the sum to the screen, in this case the sum of the digits from 100! is 648


# References
# factorial function: https://stackoverflow.com/questions/5136447/function-for-factorial-in-python
# digit sum - https://stackoverflow.com/questions/14939953/sum-the-digits-of-a-number-python
