"""
At a particular university, letter grades are mapped to grade points in the following manner:
        Letter      Grade points
        A+          4.0
        A           4.0
        A-          3.7
        B+          3.3
        B           3.0
        B-          2.7
        C+          2.3
        C           2.00
        C-          1.7
        D+          1.3
        D           1.0
        F           0.0

Write a program that begins by reading a letter grade form the user. Then your program should compute and display
the equivalent number of grade points. Ensure that your program generates an appropriate error message if the user
enters an invalid letter grade.
"""

letter_grade_input = input("Please enter your letter grade: ")

letter_grade = letter_grade_input.capitalize()

letter = letter_grade[0]
if len(letter_grade) == 2:
    symbol = letter_grade[1]
else:
    symbol = ""

if letter == "A":
    number_grade = 4.0
    if symbol == "+":
        number_grade += 0.3
    elif symbol == "-":
        number_grade -= 0.3
    else:
       number_grade = "is not recognised as a valid"
elif letter == "B":
    number_grade = 3.0
    if symbol == "+":
        number_grade += 0.3
    elif symbol == "-":
        number_grade -= 0.3
    else:
        number_grade = "is not recognised as a valid"
elif letter == "C":
    number_grade = 2.0
    if symbol == "+":
        number_grade += 0.3
    elif symbol == "-":
        number_grade -= 0.3
    else:
        number_grade = "is not recognised as a valid"
elif letter == "D":
    number_grade = 1.0
    if symbol == "+":
        number_grade += 0.3
elif letter == "F":
    number_grade = 0.0
else:
    number_grade = "is not recognised as a valid"


print(f"The grade {letter_grade} is {number_grade} grade points.")
