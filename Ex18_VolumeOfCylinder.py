""" Calculate the volume of a cylinder.
Read the radius and height from user.
Round result to one dp. """

radius = float(input("What is the radius of the cylinder? "))
height = float(input("What is the height of the cylinder? "))
pi = 3.14  # setting the value of pi
volume = 2*pi*radius*height
volume_2dp = round(volume, 1)

print("The volume of the cylinder rounded to two decimal places is: ", volume_2dp)