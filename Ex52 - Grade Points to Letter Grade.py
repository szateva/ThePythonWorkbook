"""
In the previous exercise you created a program that converts a letter grade into the equivalent number of grade points.
In this exercise you will create a program that reverses the process and converts from a grade point value entered by
the user to a letter grade. Ensure that your program handles grade point values tha gall between letter grades. Those
should be rounded to the closest letter grade. Your program should report A+ for a 4.0 (or a greater) grade point average.
"""

grade_point = float(input("Please, enter your grade point: "))

if grade_point > 4:
    grade_letter = "A+"
elif 3.7 < grade_point <= 4:
    grade_letter = "A"
elif 3.3 < grade_point <= 3.7:
    grade_letter = "A-"
elif 3.0 < grade_point <= 3.3:
    grade_letter = "B+"
elif 2.7 < grade_point <= 3.0:
    grade_letter = "B"
elif 2.3 < grade_point <=2.7:
    grade_letter = "B-"
elif 2.0 < grade_point <= 2.3:
    grade_letter = "C+"
elif 1.7 < grade_point <= 2.0:
    grade_letter = "C"
elif 1.3 < grade_point <= 1.7:
    grade_letter = "C-"
elif 1.0 < grade_point <= 1.3:
    grade_letter = "D+"
elif 0 < grade_point <= 1:
    grade_letter = "D"
elif grade_point == 0:
    grade_letter = "F"
else:
    grade_letter = "not a valid grade point for a"

print(f"{grade_point} grade point is {grade_letter} letter grade.")