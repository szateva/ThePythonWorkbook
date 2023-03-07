"""
Create a program that reads a duration from the user as a number of days, hours, minutes, and seconds.
Compute and display the total number of seconds represented by this duration.
"""

days = int(input("How many days are in the duration? "))
hours = int(input("How many hours are in the duration? "))
minutes = int(input("How many minutes are in the duration? "))
seconds = int(input("How many seconds are in the duration? "))

total_seconds = seconds + (minutes * 60) + (hours * 60*60) + (days * 24*60*60)

print(f"There are {total_seconds} seconds in {days} days, {hours} hours, {minutes} minutes and {seconds} seconds.")