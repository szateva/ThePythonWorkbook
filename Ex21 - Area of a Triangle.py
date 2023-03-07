""" The area of a triangle can be computed using the following formula, where
    b is the length of the base of the trianble, and
    h is its height:
    area = (b * h)/2

    Write a programme that allows the user to enter values for b and h.
    The program should then compute and display the area of the triangle with base length b and height h."""

base = int(input("What is the base of the triangle? "))
height = int(input("What is the height of the triangle? "))

area_triangle = (base * height)/2

print("The area of the triangle with base", base, "and height", height, "is", area_triangle )