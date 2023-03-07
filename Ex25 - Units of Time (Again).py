"""
In this exercise you will reverse teh process described in the previous exercise.
Develop a program that begins by reading a number of seconds from the user.
Then your program should display the equivalent amount of time in the form:
D:HH:MM:SS, where D, HH, MM and SS represent days, hours, minutes and seconds respectively.
The hours, minutes, and seconds should all be formatted so that they occupy exactly two digits,
with a leading 0 displayed if necessary.

// floor division i.e. 7 // 2 = 3
% modulus i.e. 7 % 2 = 1

using 0Nd for padding to achieve the desired digital time display
"""

total_seconds = int(input("How many seconds are in the duration? "))

seconds_in_days = 24*60*60
seconds_in_hours = 60*60
seconds_in_minutes = 60

days = total_seconds // seconds_in_days
remainder_after_days = total_seconds % seconds_in_days

hours = remainder_after_days // seconds_in_hours
remainder_after_hours = remainder_after_days % seconds_in_hours

minutes = remainder_after_hours // seconds_in_minutes
remainder_after_minutes = remainder_after_hours % seconds_in_minutes

seconds = remainder_after_minutes

# print(f"There are {days} days, {hours} hours, {minutes} minutes and {seconds} seconds in {total_seconds} seconds.")
print(f"{days}:{hours:02d}:{minutes:02d}:{seconds:02d}")