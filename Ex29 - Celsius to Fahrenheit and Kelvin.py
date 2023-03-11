"""
Write a program that begins by reading a temperature from the user in degrees Celsius. Then your program should
display the equivalent temperature in degrees Fahrenheit and Kelvin. The calculations needed to convert between
different units of temperature can be found on the internet.
"""

celsius = float(input("What is the temperature in degrees Celsius? "))

fahrenheit = 32 + celsius*(9/5)
kelvin = celsius + 273

print(celsius, "degrees Celsius is", round(fahrenheit,1), "degrees Fahrenheit and", kelvin, "degrees Kelvin")