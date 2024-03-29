"""Write a program that displays a conversion table from degrees Celsius to degrees Fahrenheit. The table should include
rows for all temperatures between 0 and 100 degrees Celsius that are multiples of 10 degrees Celsius. Include appropriate
headings on your columns. The formula for converting between degrees Celsius and degrees Fahrenheit can be found on the
internet."""

print("Celsius\tFarenheit")
for celsius in range(0, 101, 10):
    farenheit = (celsius * 9 / 5) + 32
    print(f"{celsius}\t\t{farenheit:.1f}")
