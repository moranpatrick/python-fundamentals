# Problem 2 - Write a program that prints the current time and date to the console.
# This program displays the current date and time on the console screen.
# Author - Patrick Moran g00179039

import datetime # import required for data nad time 

# Variable to store the current date and time
curr_date_and_time = datetime.datetime.now()

# Display The full Timestamp to the Console
print("The Current Date And Time Stamp is %s" % curr_date_and_time)

# Display the date
print("Todays Date is: %s" % curr_date_and_time.strftime("%Y-%m-%d"))

# Display the current Time in Hours And Minutes
print("The Current Time is: %d:%d" % (curr_date_and_time.hour, curr_date_and_time.minute))

# References
# https://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/
