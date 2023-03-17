"""
The horoscopes commonly reported in newspapers use the position of the sun at the time of one's birth to try and
predict the future. This system of astrology divides teh year into twelve zodiac signs, as outlined in the table
below:
            Zodiac sign         Date range
            Capricorn           Dec 22 to Jan 19
            Aquarius            Jan 20 to Feb 18
            Pisces              Feb 19 to Mar 20
            Aries               Mar 21 to Apr 19
            Taurus              Apr 20 to May 20
            Gemini              May 21 to Jun 20
            Cancer              Jun 21 to Jul 22
            Leo                 Jul 23 to Aug 22
            Virgo               Aug 23 to Sep 22
            Libra               Sep 23 to Oct 22
            Scorpio             Oct 23 to Nov 21
            Sagittarius         Nov 22 to Dec 21

Write a program that asks the user to enter his of her month and day of birth. Then your program should report the
user's zodiac sign as part of an appropriate output message.
"""

month = input("Please, enter your birth month in full: ")
day = int(input("Please, enter your day of birth: "))

if month == "December":
    if day <= 21:
        zodiac = "Sagittarius"
    else:
        zodiac = "Capricorn"
elif month == "January":
    if day <= 19:
        zodiac = "Capricorn"
    else:
        zodiac = "Aquarius"
elif month == "February":
    if day <= 18:
        zodiac = "Aquarius"
    else:
        zodiac = "Pisces"
elif month == "March":
    if day <= 20:
        zodiac = "Pisces"
    else:
        zodiac = "Aries"
elif month == "April":
    if day <= 19:
        zodiac = "Aries"
    else:
        zodiac = "Taurus"
elif month == "May":
    if day <= 20:
        zodiac = "Taurus"
    else:
        zodiac = "Gemini"
elif month == "June":
    if day <= 20:
        zodiac = "Gemini"
    else:
        zodiac = "Cancer"
elif month == "July":
    if day <= 22:
        zodiac = "Cancer"
    else:
        zodiac = "Leo"
elif month == "August":
    if day <= 22:
        zodiac = "Leo"
    else:
        zodiac = "Virgo"
elif month == "September":
    if day <= 23:
        zodiac = "Virgo"
    else:
        zodiac = "Libra"
elif month == "October":
    if day <= 22:
        zodiac = "Libra"
    else:
        zodiac = "Scorpio"
elif month == "November":
    if day <= 21:
        zodiac = "Scorpio"
    else:
        zodiac = "Saggitarius"
else:
    zodiac = ""

if zodiac == "":
    print("Sorry, something went wrong.")
else:
    print(f"{month} {day} is a(n)July {zodiac} in the zodiac signs.")