"""
The year is divided into four seasons: spring, summer, fall and winter. While the exact dates that the seasons change
vary a little bit from year to year because of the way that the calendar is constructed, we will use the following dates
for this exercise:
        Season          First day
        Spring          March 20
        Summer          June 21
        Fall            September 22
        Winter          December 21
Create a program that reads a month and a day from the user. The user will enter the name of the month as a string,
followed by the day within the month as an integer. Then your program should display the season associated with the date
that was entered.
"""

month = input("Please, enter a month: ")
day = int(input("Please, enter a day within the month you entered above: "))

if ((month == "March") and (day >= 20)) or (month == "April") or (month == "May") or ((month == "June") and (day < 21)):
    season = "Spring"
elif ((month == "June") and (day >= 21)) or (month == "July") or (month == "August") or ((month == "September") and (day < 22)):
    season = "Summer"
elif ((month == "September") and (day >= 22)) or (month == "October") or (month == "November") or ((month == "December") and (day < 21)):
    season = "Fall"
else:
    season = "Winter"

print(f"{month} {day} is {season}")

