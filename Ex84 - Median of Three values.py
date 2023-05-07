"""Write a function that takes three numbers as parameters, and returns the median value of those parameters as its result.
Include a main program that reads three values from the user and displays their median.

Hint: The median value is the middle of the three values when they are sorted into ascending order. It can be found using
if statements, or with a little bit of mathematical creativity."""

def median(a, b, c):
    list = [a, b, c]
    list.sort()
    return list[1]

a = float(input("Please, enter the first number: "))
b = float(input("Please, enter the second number: "))
c = float(input("Please, enter the third number: "))
print(f"The median of {a}, {b} and {c} is {median(a, b, c)}.")

