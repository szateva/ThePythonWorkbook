"""Create a programme that reads the length and width of a farmer's field from the user in feet.
Display the area of the field in acres.
Hint: There are 43,560 square feet in an acre"""

length_of_room = float(input("Please, enter the length of the room in feet: "))
width_of_room = float(input("Please, enter the width of the room in feet: "))
area = length_of_room * width_of_room
area_in_acre = round(area/43560, 2)
print("The area of the field is", area_in_acre, "acre.")