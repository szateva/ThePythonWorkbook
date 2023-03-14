"""
My extension for classifying triangles.
Read 3 sides from the user, then check if they make a valid triangle. If the 3 sides make a valid triangle classify
them using the below description from ex40. If the 3 sides do not make a valid triangle display a suitable error
message, not forgetting about negative numbers.

A triangle can be classified based on the length of its sides as equilateral, isosceles or scalene. All 3 sides of an
equilateral triangle have the same length. An isosceles triangle has two sides that are the same length, and a third
side that is a different length. If all sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of 3 sides of a triangle from the user. Display a message indicating the
type of the triangle.
"""

side1 = float(input("What is the length of the first side of your triangle? "))
side2 = float(input("What is the length of the second side of your triangle? "))
side3 = float(input("What is the length of the third side of your triangle? "))

if (side1 < 0) or (side2 < 0) or (side3 < 0):
    print("The sides of a triangle have to be positive!")
elif (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
    if side1 == side2 == side3:
        print(
            "A triangle with sides {0}, {1} and {other} is an equilateral triangle.".format(side1, side2, other=side3))
    elif (side1 == side2) or (side2 == side3) or (side1 == side3):
        print("A triangle with sides {0}, {1} and {other} is an isosceles triangle.".format(side1, side2, other=side3))
    else:
        print("A triangle with sides {0}, {1} and {other} is a scalene triangle.".format(side1, side2, other=side3))
else:
    print("The three sides {0}, {1} and {other} does not make a triangle.".format(side1, side2, other=side3))