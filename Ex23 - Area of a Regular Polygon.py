"""A polygon is regular if its sides are all the same length and the angles between all of the adjacent sides are equal.
    The area of a regular polygon can be computed using the following formula, where
    s is the length of the side and
    n is the number of sides:
    ares = (n * s^2)/(4*tan(pi/n))

    Write a program that reads s and n from the user and then displays the area of a regular polygon
    constructed from these values."""

import math

number_of_sides = int(input("How many sides the regular polygon has? "))
side = int(input("How many cm is each side of the regular polygon? "))


area_regular_polygon = round((number_of_sides * side**2)/(4*math.tan(math.pi/number_of_sides)), 2)

print("The area of a {0} sided polygon, whose sides are {1} cm long is {other} cm2".format(number_of_sides, side, other=area_regular_polygon))