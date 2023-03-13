"""
A triangle can be classified based on the length of its sides as equilateral, isosceles or scalene. All 3 sides of an
equilateral triangle have the same length. An isosceles triangle has two sides that are the same length, and a third
side that is a different length. If all sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of 3 sides of a triangle from the user. Display a message indicating the
type of the triangle.
"""

side1 = int(input("What is the length of the first side of your triangle? "))
side2 = int(input("What is the length of the second side of your triangle? "))
side3 = int(input("What is the length of the third side of your triangle? "))

if side1 == side2 == side3:
    print("A triangle with sides {0}, {1} and {other} is an equilateral triangle.".format(side1, side2, other=side3))
elif (side1 == side2) or (side2 == side3) or (side1 == side3):
    print("A triangle with sides {0}, {1} and {other} is an isosceles triangle.".format(side1, side2, other=side3))
else:
    print("A triangle with sides {0}, {1} and {other} is a scalene triangle.".format(side1, side2, other=side3))