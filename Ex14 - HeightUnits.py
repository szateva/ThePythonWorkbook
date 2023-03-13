""" read from the user the number of feet and the number of inches
 compute and display the equivalent height in cm"""

feet = int(input("How many feet in your height? "))
inch = int(input(("How many inches in your height? ")))
inch_in_feet = 12
heigh_inch = (feet * inch_in_feet) + inch
cm_in_inch = 2.54
cm = heigh_inch * cm_in_inch

print("Your height is %d" % cm)