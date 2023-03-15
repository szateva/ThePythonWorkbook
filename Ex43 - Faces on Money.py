"""
It is common for images of a country's previous leaders, or other individuals of historical significance, to appear
on money. The individuals that appear on banknotes in the United States are listed in Table 2.1.
Write a program that begins by reading the denomination of a banknote from the user. Then your program should display
the name of the individual that appears on the banknote of the entered amount. An appropriate message should be
displayed id no such note exist.
"""

denominion = int(input("Please, enter the value of an American note: "))

one_dollar = "George Washington"
two_dollar = "Thomas Jefferson"
five_dollar = "Abraham Lincoln"
ten_dollar = "Alexander Hamilton"
twenty_dollar = "Andrew Jackson"
fifty_dollar = "Ulysses S. Grant"
hundred_dollar = "Benjamin Franklin"

if denominion == 1:
    display = one_dollar
elif denominion == 2:
    display = two_dollar
elif denominion == 5:
    display = five_dollar
elif denominion == 10:
    display = ten_dollar
elif denominion == 20:
    display = twenty_dollar
elif denominion == 50:
    display = fifty_dollar
elif denominion == 100:
    display = hundred_dollar
else:
    display = ""

if display == "":
    print(f"Sorry, there are no American notes of the value ${denominion}")
else:
    print(f"{display} is pictured on the ${denominion} note.")