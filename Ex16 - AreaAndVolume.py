""" read radius r from the user
 compute and display the area of a circle with radius r
 compute and display the volume of a sphere with radius r
 use the pi constant from the math module"""
import math

r = float(input("What is the radius? "))
area_circle = (r**2)*math.pi
print("The area of a circle with radius %d is %.2f" %(r, area_circle))
volume_sphere = (4/3)*math.pi*(r**3)
print("The volume of a sphere with radius %d is %.2f" %(r, volume_sphere))