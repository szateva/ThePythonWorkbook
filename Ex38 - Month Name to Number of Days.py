"""
The length of each month varies between 28 to 31 days. In this exercise you will create a program that reads the
name of a month from the user as a string. Then your program should display the number of days in that month. Display
'28 or 29 days' for February so that leap years are addressed.
"""

month = input("Which month would you like to check? ")

days_30 = ["April", "June", "September", "November"]
days_31 = ["January", "March", "May", "July", "August", "October", "December"]

if month in days_30:
    print(month, "has 30 days.")
elif month in days_31:
    print(month, "has 31 days.")
elif month == "February":
    print(month, "has 28 or 29 days.")
else:
    print("Sorry, I cannot find your month. Do you have a typing mistake in your answer?")
