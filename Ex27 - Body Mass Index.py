"""
Write a program that computes the body mass indec (BMI) of an individual.
Your program should begin by reading a height and weight from the user.
Then it should use one of the following two formulas to compute the BMI before displaying it.

If you read the height in inches and the weight in pounds then the BMI index is computed using the following formula:
BMI = weight/(height*weight)*703

If you read the height in meters and the weight in kilograms the body mass index is computed using
this slightly simpler formula:
BMI = weight/(height * weight)
"""

height = float(input("What is your height in meters? "))
weight = float(input("What is your weight in kilograms? "))

BMI = round(weight/(height*weight),2)

print("Your BMI is", BMI)