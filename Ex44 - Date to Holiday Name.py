"""
Canada has three national holidays which fall on the same dates each year.
        Holiday             Date
        New year's day      January 1
        Canada day          July 1
        Christmas day       December 25

Write a program that reads a month and a day from the user. If the month and the day match one of the holidays listed
previously then your program should display the holiday's name Otherwise your program should indicate that the entered
month and day do not correspond to a fixed-date holiday.
"""
month = input("Please enter a month: ")
day = input("Please enter a day (1 to 31): ")

january_1 = "New year's day"
july_1 = "Canada day"
december_25 = "Christmas day"

if (month == "January") and (day == "1"):
    holiday_name = january_1
elif (month == "July") and (day == "1"):
    holiday_name = july_1
elif (month == "December") and (day == "25"):
    holiday_name = december_25
else:
    holiday_name = ""

if holiday_name == "":
    print(f"Sorry, Canada has no fixed-date holiday on {month} {day}")
else:
    print(f"{month} {day} is {holiday_name}")

