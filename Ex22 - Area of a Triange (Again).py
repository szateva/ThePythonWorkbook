""" In the previous exercise you created a program that computed the area of a triangle when the length of its base
    and height were known. It is also possible to compute the area of a triangle when the lengths of all three sides
    are known. Let s1, s2 and s3 be the lengths of the sides. Let s = (s1 + s2 + s3)/2. Then the area of the triangle
    can be calculated using the following formula:

    area = sqrt(s*(s-s1)*(s-s2)*(s-s3))

    Develop a program that reads the lengths of the sides of the triangle from the user and displays its area.
"""
import math

side1 = int(input("What is the length of the first side of the triangle? "))
side2 = int(input("What is the length of the second side of the triangle? "))
side3 = int(input("What is the length of the third side of the triangle? "))
side = (side1 + side2 + side3)/2

area = math.sqrt(side*(side - side1)*(side - side2)*(side - side3))

print("The area of the triangle whose sides are", side1, ",", side2, "and", side3, "is", area) # this version doesn't display nicely, there is space between 3 and the .
print('The area of the triangle whose sides are {0}, {1}, and {2} is {other}.'.format(side1, side2, side3, other=area)) #str.format works well but need to pay attention to positioning