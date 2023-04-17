""" Redoing the previous exercise using tabulate module, following this YouTube video:
https://www.youtube.com/watch?v=Smf68icE_as"""

"""Write a program that displays a conversion table from degrees Celsius to degrees Fahrenheit. The table should include
rows for all temperatures between 0 and 100 degrees Celsius that are multiples of 10 degrees Celsius. Include appropriate
headings on your columns. The formula for converting between degrees Celsius and degrees Fahrenheit can be found on the
internet."""

from tabulate import tabulate

table = []
for celsius in range(0, 101, 10):
    farenheit = (celsius * 9 / 5) + 32
    table.append([celsius, f"{farenheit:}"])
print(tabulate(table, headers=["Celsius", "Farenheit"], tablefmt="fancy_grid"))