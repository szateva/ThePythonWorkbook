"""
It is commonly said that one human year is equivalent to 7 dog years. However, this simple conversion fails to recognise
that dogs reach adulthood in approximately 2 years. As a result, some people believe that it is better to count
each of the first two human years as 10.5 dog years, and then count each additional human years as 4 dog years.
Write a program that implements the conversion from human years to dog Years described in the previous paragraph.
Ensure that your program works correctly for conversion of less than 2 human years and for conversions of two or more
human years. Your program should display an appropriate error message if the user enters a negative number.
"""

human_years = float(input("How many human years you would like to convert to dog years? "))

if human_years < 0:
    print("Sorry, years have to be positive numbers.")
elif 0 <= human_years <= 2:
    dog_years = human_years * 10.5
    print(human_years, "are", round(dog_years, 2), "dog years")
else:
    dog_years = human_years * 4
    print(human_years, "human years are", round(dog_years, 2), "dog years")