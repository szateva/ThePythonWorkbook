"""
The Chinese zodiac assigns animals to years in a 12-year cycle. One 12 year cycle is shown in the table below.
The pattern repeats from there, with 2012 being another year of the dragon, and 1999 being another year of the hare.
        Year        Animal
        2000        Dragon
        2001        Snake
        2002        Horse
        2003        Sheep
        2004        Monkey
        2005        Rooster
        2006        Dog
        2007        Pig
        2008        Rat
        2009        Ox
        2010        Tiger
        2011        Hare
Write a program that reads a year from the user and displays the animal associated with that year. Your program
should work correctly for any year greater than of equal to zero, not just the ones in the table.
"""

year = int(input("Please, enter the year you were born: "))

if (year % 12) == 8:
    chinese_zodiac = "Dragon"
elif (year % 12) == 9:
    chinese_zodiac = "Snake"
elif (year % 12) == 10:
    chinese_zodiac = "Horse"
elif (year % 12) == 11:
    chinese_zodiac = "Sheep"
elif (year % 12) == 0:
    chinese_zodiac = "Monkey"
elif (year % 12) == 1:
    chinese_zodiac = "Rooster"
elif (year % 12) == 2:
    chinese_zodiac = "Dog"
elif (year % 12) == 3:
    chinese_zodiac = "Pig"
elif (year % 12) == 4:
    chinese_zodiac = "Rat"
elif (year % 12) == 5:
    chinese_zodiac = "Ox"
elif (year % 12) == 6:
    chinese_zodiac = "Tiger"
else:
    chinese_zodiac = "Hare"

print(f"The year {year} is the year of the {chinese_zodiac} in the Chinese zodiac.")