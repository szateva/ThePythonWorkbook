""" user to enter the longitude and latitude of two points on Earth
 Calculate the distance between them in km
 formula used for distance is given in the book"""
import math

t1 = float(input("Give the latitude of point 1: "))
g1 = float(input("Give the latitude of point 1: "))
t2 = float(input("Give the latitude of point 2: "))
g2 = float(input("Give the latitude of point 2: "))

rad_t1 =math.radians(t1)
rad_g1 = math.radians(g1)
rad_t2 = math.radians(t2)
rad_g2 = math.radians(g2)
earth_radius = 6371.01

distance = earth_radius*math.acos( math.sin(rad_t1) * math.sin(rad_t2) + math.cos(rad_t1) * math.cos(rad_t2)*math.cos(rad_g1 - rad_g2))
print("The distance between the two points in km is: ", round(distance,2))