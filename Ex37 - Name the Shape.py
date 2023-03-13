"""
Write a program that determines the name of a shape from its number of sides. Read the number of sides from the user
and then report the appropriate name as part of a meaningful message. Your program should support shapes with anywhere
from 3 up (and including) 10 sides. If a number of sides outside of this range is entered then your program should
display an appropriate error message.
"""

no_of_sides = int(input("How many sides does your shape have? "))
list_of_shapes = ["triangle", "quadrilateral", "pentagon", "hexagon", "heptagon", "octagon", "nonagon", "decagon"]

if 3 <= no_of_sides <= 10:
    print("A", no_of_sides, "sided shape is a", list_of_shapes[no_of_sides-3])
else:
    print("The number you entered is not in the scope of this program.")
