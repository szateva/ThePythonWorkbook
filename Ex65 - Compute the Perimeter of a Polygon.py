""" Write a program that computed the perimeter of a polygon. Begin by reading the x, y coordinates for the first point
on the perimeter of the polygon from the user. Then continue reading pairs of x, y values until the user enters a blank
line for the x-coordinate. Each time you read an additional coordinate you should compute the distance to the previous
and add it to the perimeter. When a blank line is entered for the x-coordinate your program should add the distance from
the last point to the first point to the perimeter. Then it should display the total perimeter. Sample input and output
is shown below, with the user’s input shown in bold:
Enter the x part of the coordinate: 0
Enter the y part of the coordinate: 0
Enter the x part of the coordinate: (blank to quit): 1
Enter the y part of the coordinate: 0
Enter the x part of the coordinate: (blank to quit): 0
Enter the y part of the coordinate: 1
Enter the x part of the coordinate: (blank to quit):
The perimeter of that polygon is 3.414213562373095 """

import math

x_coord_list = []
y_coord_list = []
perimeter = 0

x_coord = input("Enter the x part of the coordinate: ")
y_coord = input("Enter the y part of the coordinate: ")

while x_coord != "":
    x_coord_list.append(float(x_coord))
    y_coord_list.append(float(y_coord))
    x_coord = input("Enter the x part of the coordinate (blank to quit): ")
    y_coord = input("Enter the y part of the coordinate (blank to quit): ")

for i in range(len(x_coord_list) - 1):
    distance = math.sqrt((x_coord_list[i + 1] - x_coord_list[i]) ** 2 + (y_coord_list[i + 1] - y_coord_list[i]) ** 2)
    perimeter += distance
distance = math.sqrt((x_coord_list[0] - x_coord_list[-1]) ** 2 + (y_coord_list[0] - y_coord_list[-1]) ** 2)
perimeter += distance
print(f"The perimeter of that polygon is {perimeter:.4f} ")