"""Write a program that asks the user to enter the width and length of a room.
Once the values had been read, your programme should compute and display the area of the room.
The length and width will be entered as floating point numbers.
Include units in your prompt and output message: either feet or meters
depending on which units you are more comfortable working with"""

length_of_room = float(input("Please, enter the length of the room in meters: "))
width_of_room = float(input("Please, enter the width of the room in meters: "))
area = length_of_room * width_of_room
print("The area of the room is", area, "square meters")