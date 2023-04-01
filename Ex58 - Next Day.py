"""
Write a program that reads a date from the user and computes its immediate successor. For example, if the user enters
values that represent 2013-11-18 then your program should display a message indicating that the day immediately
after 2013-11-18 is 2013-11-19. If the user enters values that represent 2013-11-30 then the program should indicate
that the next day is 2013-12-01. If the user enters values that represents 2013-12-31 then the program should indicate
that the next day is 2014-01-01. The date will be entered in numeric form with three separate input statements; one for
the year, one for the month, and one for the day. Ensure that your program works correctly for leap years.
"""

year = int(input("Please, enter a year in numerical form: "))
month = int(input("Please, enter a month in numerical form: "))
day = int(input("Please, enter a day in numerical form: "))

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


if (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10):
    if 1 <= day <= 30:
        new_day = day + 1
        next_date = f"{year:0>4d}-{month:0>2d}-{new_day:0>2d}"
    elif day == 31:
        new_month = month + 1
        new_day = 1
        next_date = f"{year:0>4d}-{new_month:0>2d}-{new_day:0>2d}"
    else:
        next_date = f"{year:0>4d}-{month:0>2d}-{day:0>2d} is not a valid date."
elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
    if 1 <= day <= 29:
        day += 1
        next_date = f"{year:0>4d}-{month:0>2d}-{day:0>2d}"
    elif day == 30:
        new_month = month + 1
        new_day = 1
        next_date = f"{year:0>4d}-{new_month:0>2d}-{new_day:0>2d}"
    else:
        next_date = f"{year:0>4d}-{month:0>2d}-{day:0>2d} is not a valid date."
elif month == 12:
    if 1 <= day <= 30:
        new_day = day + 1
        next_date = f"{year:0>4d}-{month:0>2d}-{new_day:0>2d}"
    elif day == 31:
        new_year = year + 1
        new_month = 1
        new_day = 1
        next_date = f"{new_year:0>4d}-{new_month:0>2d}-{new_day:0>2d}"
    else:
        next_date = f"{year:0>4d}-{month:0>2d}-{day:0>2d} is not a valid date."
else:
    if 1 <= day <= 27:
        new_day = day + 1
        next_date = f"{year:0>4d}-{month:0>2d}-{new_day:0>2d}"
    elif day == 28:
        if leap == True:
            new_day = 29
            next_date = f"{year:0>4d}-{month:0>2d}-{new_day:0>2d}"
        else:
            new_month = month + 1
            new_day = 1
            next_date = f"{year:0>4d}-{new_month:0>2d}-{new_day:0>2d}"
    elif day == 29:
        if leap == True:
            new_month = month + 1
            new_day = 1
            next_date = f"{year:0>4d}-{new_month:0>2d}-{new_day:0>2d}"
        else:
            next_date = f"{year:0>4d}-{month:0>2d}-{day:0>2d} is not a valid date."
    else:
        next_date = f"{year:0>4d}-{month:0>2d}-{day:0>2d} is not a valid date."

print(f"The date following {year:0>4d}-{month:0>2d}-{day:0>2d} is {next_date} ")
