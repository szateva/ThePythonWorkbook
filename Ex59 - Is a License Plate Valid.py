"""
In a particular jurisdiction, older  license plates consist of three uppercase letters followed by three numbers.
When all of the license plates following that pattern had been used, the format was changed to four numbers followed by
three uppercase letters.
Write a program tht begins by reading a string of characters from the user. Then your program should display a message
indicating whether the characters are valid for an old style license plate or a new style license plate. Your program
should display an appropriate message if the string entered by the user is not valid for either style of license plate.
"""

plate = input("Please, enter the license plate: ")

if len(plate) > 6:
    print(f"The license plate {plate} is not a valid format.")
elif plate.isalnum() == False:
    print(f"The license plate {plate} is not a valid format.")
elif (plate[:3].isupper() == True) and (plate[4:].isnumeric() == True): # checks old style license plate
    print(f"The license plate {plate} is old style.")
elif (plate[:3].isnumeric() == True) and (plate[4:].isupper() == True): # checks new style license plate
    print(f"The license plate {plate} is new style.")
else:
    print(f"The license plate {plate} is not a valid format.")