# Problem 9 - Source: https://tour.golang.org/flowcontrol/8

# Implement the square root function using Newton’s method. In this case, Newton’s method is to approximate sqrt(x) 
# by picking a starting point z and then repeating:
# z_next = z - ((z*z - x) / (2 * z))

# To begin with, just repeat that calculation 10 times and see how close you get to the answer for various 
# values (1, 2, 3, …). Next, change the loop condition to stop once the value has stopped changing 
# (or only changes by a very small delta). How close are you to the math.sqrt value?

# Author: Patrick Moran g00179039

import math

# z = estimate
# x = number
def func1(n, e):
    print("Loop 10 times using th given formula z_next = z - ((z*z - x) / (2 * z))")
    for i in range(0,10): # Loop 10 times and print the result
        e = e - ((e*e - n) / (2 * e))
        print(e)

def func2(n, e):
    print("Loop until the value has stopped changing or only changes by a very small delta")
    # Create a copy of the original estimate
    prevEstimate = e
    running = False

    e = e - ((e*e - n) / (2 * e))

    while running == False:
        if prevEstimate == e: # They are the same stop the loop
            print(e)
            running = True
        else: # Otherwise keep trying
            print(e)
            prevEstimate = e
            e = e - ((e*e - n) / (2 * e))
    return e # Return the estimate

# Collect values from user
print("Enter a value you want to get the square root of: ")
num = int(input())
print("Enter your estimate: ")
est = int(input())

# Call function which loops just 10 times
func1(num, est)
# Call the function that uses a loop to stop
estimateAnswer = est = func2(num, est)

# Answer using math.sqr root
ans = math.sqrt(num)
# Difference between the two
difference = estimateAnswer - ans
print("The Difference between math.sqrt and newtons method is %f." % difference)
