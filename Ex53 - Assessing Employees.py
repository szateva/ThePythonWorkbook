"""
At a particular company, employees are rated at the end of each year. The rating scale begins at 0.0, with higher values
indicating better performance and resulting in larger raises. The value awarded to an employee is either 0.0, 0.4 or
0.6 or more. Values between 0.0 and 0.4, and between 0.4 and 0.6 are never used. The meaning associated with each rating
is shown in the following table. The amount of an employee's raise is $2400.00 multiplied by their rating.
        Rating      Meaning
        0.00        Unacceptable performance
        0.4         Acceptable performance
        0.6         Meritorious performance

Write a program that reads a rating from the user and indicated whether the performance was unacceptable, acceptable or
meritorious. The amount of an employee's raise should also be reported. Your program should display an appropriate error
message if an invalid rating is entered.
"""

base_raise = 2400.00
rating_num1 = 0.0
rating_num2 = 0.4
rating_num3 = 0.6

employee_rating = float(input("Please, enter your rating: "))

if employee_rating == rating_num1:
    rating_words = "Unacceptable performance"
    bonus = base_raise * rating_num1
elif employee_rating == rating_num2:
    rating_words = "Acceptable performance"
    bonus = base_raise * rating_num2
elif employee_rating == rating_num3:
    rating_words = "Meritorious performance"
    bonus = base_raise * rating_num3
else:
    rating_words = "is not a valid rating"
    bonus = 0

print(f"{employee_rating} is a(an) {rating_words} and your bonus is ${bonus}.")