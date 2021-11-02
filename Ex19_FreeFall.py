""" Calculate the speed at impact (hitting the ground) of an object.
 User to supply initial height, initial speed to be 0 and acceleration is to be 9.81 m/s^2.
 Use formula vf = sqrt(vi^2 + 2ad) where d is the starting height (distance) in meters supplied by the user."""
import math

d = int(input("What height is the object when dropped? "))

vi = 0      #initial speed, set to 0 m/s
a = 9.81    # acceleration (gravitational pull of Earth), set to 9.81 m/s^2

vf = math.sqrt(vi**2 + a*d) # formula to calculate final speed, given by task
vf_rounded = round(vf, 2)   # final speed to round to 2 dp

print("The final speed with which the object will hit the ground is: ", vf_rounded)
