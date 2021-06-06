""" read distance in feet from the user
 convert to: inches, yards and miles"""
inch_in_feet = 12
feet_in_yard = 3
feet_in_mile = 5280

distance_in_feet = int(input("What is the distance in feet? "))

distance_in_inch = distance_in_feet * inch_in_feet
distance_in_yard = distance_in_feet / feet_in_yard
distance_in_mile = distance_in_feet / feet_in_mile

print("%d feet is %d inches" % (distance_in_feet, distance_in_inch))
print("%d feet is %.2f yard" % (distance_in_feet, distance_in_yard))
print("%d feet is %.2f miles" % (distance_in_feet, distance_in_mile))