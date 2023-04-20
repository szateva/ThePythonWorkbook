""" Exercise 51 included a table that shows the conversion from letter grades to grade points at a particular academic
institution. In this exercise you will compute the grade point average of an arbitrary number of letter grades entered
by the user. The user will enter a blank line to indicate that all of the grades have been provided. For example,
if the user enters A, followed by C+, followed by B, followed by a blank line then your program should report a grade
point average of 3.1.
You may find your solution to Exercise 51 helpful when completing this exercise. Your program does not need to do any
error checking. It can assume that each value entered by the user will always be a valid letter grade or a blank line. """

#TODO - create a few test cases to ensure the program works as expected

A_plus = 4.0
A = 4.0
A_minus = 3.7
B_plus = 3.3
B = 3.0
B_minus = 2.7
C_plus = 2.3
C = 2.0
C_minus = 1.7
D_plus = 1.3
D = 1.0
F = 0.0

grade = input("Please enter your letter grade: ")
average = 0
sum = 0
count = 0

while grade != "":
    grade = grade.upper()
    if (grade == "A+") or (grade == "A"):
        sum += A_plus
        count += 1
    elif grade == "A-":
        sum += A_minus
        count += 1
    elif grade == "B+":
        sum += B_plus
        count += 1
    elif grade == "B":
        sum += B
        count += 1
    elif grade == "B-":
        sum += B_minus
        count += 1
    elif grade == "C+":
        sum += C_plus
        count += 1
    elif grade == "C":
        sum += C
        count += 1
    elif grade == "C-":
        sum += C_minus
        count += 1
    elif grade == "D+":
        sum += D_plus
        count += 1
    elif grade == "D":
        sum += D
        count += 1
    elif grade == "F":
        sum += F
        count += 1
    grade = input("Please enter your letter grade: (blank to quit) ")
average = sum / count
print(f"Your average grade is {average:.2f}.")