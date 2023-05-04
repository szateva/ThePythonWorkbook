""" Write a function that takes the lengths of the two shorter sides of a right triangle as its parameters. Return the
hypotenuse of the triangle, computed using Pythagorean theorem, as the function’s result. Include a main program that
reads the lengths of the shorter sides of a right triangle from the user, uses your function to compute the length of
the hypotenuse, and displays the result. """

from math import sqrt

def hypotenuse(a, b):
    return sqrt(a ** 2 + b ** 2)

a = float(input("Please, enter the length of the adjacent in a right angled triangle (cm): "))
b = float(input("Please, enter the length of the opposite in a right angled triangle (cm): "))

hyp = round(hypotenuse(a, b), 2)

print(f"For the triangle with adjacent {a}cm and opposite {b}cm the hypotenuse is {hyp}cm.")