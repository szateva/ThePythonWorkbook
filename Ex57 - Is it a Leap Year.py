"""
Most years have 365 days. However, the rime required for the Earth to orbit the Sun is actually slightly more than that.
As a result, an extra day, February 29, is included in some years to correct for this difference. Such years are referred
to as leap years. The rules for determining whether a year is a leap year follow:

Any year that is divisible by 400 is a leap year.
Of the remaining years, any year that is divisible by 100 is NOT a leap year.
Of the remaining years, any year that is divisible by 4 is a leap year.
All other years are NOT leap years.

Write a program that reads a year from the user and displays a message indicating whether a year is a leap year.
"""

year = int(input("Please, enter a year: "))

if (year % 400) == 0:
    leap = True
else:
    if (year % 100) == 0:
        leap = False
    else:
        if (year % 4) == 0:
            leap = True
        else:
            leap = False
if leap == True:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")